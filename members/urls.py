from django.urls import path
from .views import MemberCreateAPIView

urlpatterns = [
    path('create', MemberCreateAPIView.as_view()),
]