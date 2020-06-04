from django.urls import path
from .views import MemberCreateAPIView
from .views import MemberAuthentocateAPIView

urlpatterns = [
    path('create', MemberCreateAPIView.as_view()),
    path('auth', MemberAuthentocateAPIView.as_view()),
]