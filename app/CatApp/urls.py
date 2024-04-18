from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('Auth.urls')),
    path('api/v1/', include('Link.urls')),
    path('api/v1/', include('Collection.urls')),
]
