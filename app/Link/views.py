from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
        print("method", method)

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("This link was deleted.", status=status.HTTP_204_NO_CONTENT)
