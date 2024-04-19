from rest_framework import viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from Link.models import Link
from .models import Collection
from .serializers import CollectionSerializer, UpdateCollectionSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Collection.objects.filter(user=self.request.user)
        else:
            return Collection.objects.none()

    def get_serializer_class(self):
        method = self.action

        match method:
            case 'list':
                return CollectionSerializer
            case 'partial_update':
                return UpdateCollectionSerializer
            case _:
                return CollectionSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        link_ids = request.data.get('links')
        collection = serializer.instance

        # add each link to db
        if link_ids:
            for link_id in link_ids:
                link = get_object_or_404(Link, id=link_id, user=request.user)
                collection.links.add(link)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
