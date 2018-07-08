from django.test import TestCase
from django.urls import reverse

from blog import models
from core.constants import HTTP_STATUS_CODE


class _AbstractViewTest(TestCase):
    model = None
    url = None

    def _check_status(self, *args, status=HTTP_STATUS_CODE.OK):
        response = self.client.get(reverse(self.url, args=args))
        self.assertEqual(response.status_code, status)

    def test_view_ok(self):
        self._check_status()


class _AbstractPublicationViewTest(_AbstractViewTest):
    def setUp(self):
        self.publication = self.model.objects.create(**{'title': 'test'})

    def tearDown(self):
        self.model.objects.all().delete()

    def test_view_ok(self):
        self._check_status(self.publication.id)

    def test_view_not_found(self):
        self._check_status(self.publication.id + 1, status=HTTP_STATUS_CODE.NOT_FOUND)


class TestIndexView(_AbstractViewTest):
    url = 'blog:index'


class TestTagsView(_AbstractViewTest):
    url = 'blog:tags'


class TestCategoryView(_AbstractPublicationViewTest):
    model = models.Category
    url = f'blog:{models.Category.__name__.lower()}'


class TestTagView(_AbstractPublicationViewTest):
    model = models.Tag
    url = f'blog:{models.Tag.__name__.lower()}'
