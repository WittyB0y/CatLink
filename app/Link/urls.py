from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLinkViewSet

router = DefaultRouter()
router.register(r'links', UserLinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
