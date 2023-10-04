from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import CategoryModelViewSet, ProductModelViewSet, ProductList

router = DefaultRouter()

router.register('category', CategoryModelViewSet)
router.register('', ProductModelViewSet)

urlpatterns = [
    path('template/', ProductList.as_view()),
    path('', include(router.urls))
]
