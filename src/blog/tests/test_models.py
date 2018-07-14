from django.test import TestCase

from blog import models
from .mixins import CreateMixin


class _AbstractPublicationModelTest(TestCase):
    model = None

    def setUp(self):
        self.publication = self.model.objects.create(**{'title': 'test'})

    def tearDown(self):
        self.model.objects.all().delete()

    def test_publication(self):
        self.assertEqual(self.publication.title, 'test')

    def test_retrieve(self):
        pub = self.model.objects.get(pk=self.publication.pk)
        self.assertEqual(pub.title, self.publication.title)

    def test_update(self):
        self.publication.title = 'title'
        self.publication.save()

        pub = self.model.objects.get(pk=self.publication.pk)
        self.assertEqual(pub.title, self.publication.title)


class TestCategoryModel(_AbstractPublicationModelTest):
    model = models.Category


class TestTagModel(_AbstractPublicationModelTest):
    model = models.Tag


class TestModels(TestCase, CreateMixin):
    def test_cascade_category(self):
        self._create_objects()

        models.Category.objects.filter(pk=self.category.pk).delete()

        self.assertEqual(models.Category.objects.count(), 0)
        self.assertEqual(models.Article.objects.count(), 0)

        self._remove_objects()
