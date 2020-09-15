from django.urls import path
from .views import AddToCartAPIView
from .views import IndexAPIView

urlpatterns = [
    path('add', AddToCartAPIView.as_view()),
    path('index', IndexAPIView.as_view()),
]