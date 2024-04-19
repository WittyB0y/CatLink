from rest_framework import serializers
from Collection.models import Collection
from Link.serializers import LinkSerializer


class CreateCollectionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Collection
        fields = ['name', 'description', 'links', 'user']

    def links(self, obj):
        """to get list of ids"""
        links_obj = obj.links.all()
        return [link.id for link in links_obj]


class CollectionSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'


class UpdateCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name', 'description', 'links']

    def links(self, obj):
        """to get list of ids"""
        links_obj = obj.links.all()
        return [link.id for link in links_obj]
