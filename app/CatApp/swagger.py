from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from CatApp import settings

SCHEMA_VIEW = get_schema_view(openapi.Info(
    title="CatLink API",
    default_version='v. 1',
    contact=openapi.Contact(settings.EMAIL_HOST),
),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
