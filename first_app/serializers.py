from rest_framework import serializers
from first_app.models import Post


class PostSerializer(serializers.Serializer):
    """ convert model fields in to serializers fields """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50, required=False, allow_blank=True)
    descriptions = serializers.CharField(style={'base_template': 'textarea.html'})
    status = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """Create and return a new `Post` instance, given the validated data."""
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Update and return an existing `Post` instance, given the validated data."""
        instance.title = validated_data.get('title', instance.title)
        instance.descriptions = validated_data.get('descriptions', instance.descriptions)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
