from django.test import TestCase
from django.contrib.auth import get_user_model

from blog import models


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


class TestModels(TestCase):
    def _create_objects(self):
        self.user = get_user_model().objects.create_user(username='user', password='qwerty')
        self.category = models.Category.objects.create(title='category')
        self.article = models.Article.objects.create(
            title='article',
            author=self.user,
            category=self.category,
            content='Lorem ipsum dolor sin amet...'
        )
        self.tag = models.Tag.objects.create(title='tag')

        self.article.tags.add(self.tag)

    def _remove_objects(self):
        for model in [get_user_model(), models.Category, models.Article, models.Tag]:
            model.objects.all().delete()

    def test_cascade_category(self):
        self._create_objects()

        models.Category.objects.filter(pk=self.category.pk).delete()

        self.assertEqual(models.Category.objects.count(), 0)
        self.assertEqual(models.Article.objects.count(), 0)

        self._remove_objects()
