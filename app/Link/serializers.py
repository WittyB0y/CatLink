from rest_framework import serializers
from Link.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'description', 'url', 'image', 'link_type']


class CreateLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Link
        fields = ['id', 'url']

    def validate(self, attrs):
        if "url" not in attrs:
            raise serializers.ValidationError("Error")

        user = self.context['request'].user
        if Link.objects.filter(user=user, url=attrs["url"]).exists():
            raise serializers.ValidationError("This URL has already been added by the user.")
        return attrs


class UpdateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['url', ]


class IdLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", ]
