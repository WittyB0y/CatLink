from types import NoneType

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Tasks.background_parse_task import parse_site
from .models import Link
from .serializers import LinkSerializer, CreateLinkSerializer, UpdateLinkSerializer


class UserLinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Link.objects.filter(user=user)

    def get_serializer_class(self):
        method = self.action

        match method:
            case 'create':
                return CreateLinkSerializer
            case 'list':
                return LinkSerializer
            case 'update':
                return UpdateLinkSerializer
            case _:
                return LinkSerializer

    def perform_create(self, serializer):
        """
        set user when create Link object
        """
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        url = request.data.get('url')
        link_type = request.data.get('link_type')
        if not isinstance(url, NoneType):
            parse_site.delay(request.user.id, link_type, url)
            return Response("Task was added.", status=status.HTTP_200_OK)
        return Response("Url is required field.", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("This link was deleted.", status=status.HTTP_204_NO_CONTENT)
