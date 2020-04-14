from django.urls import path

from .views import ProductAPIView
from .views import ProductDetailAPIView

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('detail/<int:id>', ProductDetailAPIView.as_view()),
]