from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('api/products/', include('products.urls')),
    path('api/carts/', include('carts.urls')),
]


