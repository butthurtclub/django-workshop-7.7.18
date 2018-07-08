from rest_framework import serializers
from blog import models


def publication_serializer(instance_class):
    def wrap(instance):
        class Meta:
            model = instance_class
            fields = ('created', 'updated', 'title')
        instance.Meta = Meta
        return instance
    return wrap


@publication_serializer(models.Category)
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    pass


@publication_serializer(models.Tag)
class TagSerializer(serializers.HyperlinkedModelSerializer):
    pass
