from django.urls import path
from .views import MemberCreateAPIView
from .views import MemberAuthentocateAPIView
from .views import GetMemberInfoAPIView
from .views import UpdateMemberInfoAPIView

urlpatterns = [
    path('create', MemberCreateAPIView.as_view()),
    path('auth', MemberAuthentocateAPIView.as_view()),
    path('get_info', GetMemberInfoAPIView.as_view()),
    path('update', UpdateMemberInfoAPIView.as_view()),
]