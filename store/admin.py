from django.contrib import admin, messages
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.urls import reverse 
from django.utils.html import format_html, urlencode
from tags.models import TaggedItem
from . import models

# Register your models here.
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory' #it shows the name after "by" in filter area
    parameter_name = 'inventory' #it shows in link

    def lookups(self, request, model_admin):
        return [
            ('<10', 'low') #this is the first item (we can use many items)
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
    
    ### now we can use this class as a filter. (look at the ProductAdmin)



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection'] # when you creating products it dose not show all the collections, now it showing some of them and you can search them by their name. -> but first you need to create serch fields for collections.
    prepopulated_fields = {
        'slug': ['title']   # when you creating product from admin panel, slug will automaticly using title as an input
    }
    actions = ['clear_inventory']      # we created clear_inventory as an action , and we use it here. we can create and use many actions and use it in that list
    search_fields = ['title']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_filter = ['collection', 'last_update', InventoryFilter]

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
    
    @admin.action(description='Clear inventory') # it shows in top of the list when you can do some actions
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated'
        )



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']



class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']



@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']  # look at the autocomplete_fields comments in ProductAdmin.

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist') #changelist is the name of product page
            + '?' 
            + urlencode({
                'collection__id': collection.id
            }))
        return format_html('<a href={}>{}</a>', url, collection.products_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )