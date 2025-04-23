from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
# URLConf

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register(r'reviews', views.ReviewViewSet, basename='product-reviews')



urlpatterns = router.urls + router.urls + products_router.urls
