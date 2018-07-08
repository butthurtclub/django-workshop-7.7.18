from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from api import serializers
from blog import models


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    renderer_classes = (JSONRenderer,)


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    renderer_classes = (JSONRenderer,)
