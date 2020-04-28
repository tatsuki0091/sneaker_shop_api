from django.conf.urls import url
from django.urls import path, re_path
from rest_framework import routers

from .views import {
    ProductAPIView, 
    ProductDetailAPIView, 
    SearchProductsAPIView,
    GetInfoForCrouselAPIView
}

router = routers.DefaultRouter()
router.register('', ProductAPIView)

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('detail/<int:id>', ProductDetailAPIView.as_view()),
    re_path(r'^search', SearchProductsAPIView.as_view()),
    path('getFive', GetInfoForCrouselAPIView.as_view()),
]