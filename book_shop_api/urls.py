
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    url('admin/', admin.site.urls),
    url('product_api/', include('products.urls')), # 追加
    url('member_api/', include('members.urls')), # 追加
    url('cart_api/', include('carts.urls')), # 追加
]


# ↓追加
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns