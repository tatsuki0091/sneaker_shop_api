
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # 追加
    path('product_api/', include('products.urls')), # 追加
    path('member_api/', include('members.urls')), # 追加
]

