from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# URLConf

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

urlpatterns = router.urls
