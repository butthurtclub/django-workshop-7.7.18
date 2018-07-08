import ujson
from django.test import TestCase
from django.urls import reverse

from blog import models
from core.constants import HTTP_STATUS_CODE


def _publication_api_view_test(instance_class, view_type):
    def wrap(instance):
        instance.model = instance_class
        instance.url = f'api:{instance_class.__name__.lower()}-{view_type}'
        instance.view_type = view_type

        return instance
    return wrap


class _AbstractAPIViewTest(TestCase):
    model = None
    url = None
    view_type = None

    def setUp(self):
        self.publication = self.model.objects.create(**{'title': self.url})

    def tearDown(self):
        self.model.objects.all().delete()

    def _check_response(self, *args, postfix=None, status=HTTP_STATUS_CODE.OK):
        reversed_url = reverse(self.url, args=args)
        if postfix:
            reversed_url = f'{reversed_url}{postfix}/'

        response = self.client.get(reversed_url)
        self.assertEqual(response.status_code, status)
        return response

    def _check_list_data(self, response):
        data = ujson.loads(response.content)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], self.url)
        self.assertTrue('created' in data[0])
        self.assertTrue('updated' in data[0])

    def _check_detail_data(self, response):
        data = ujson.loads(response.content)
        self.assertEqual(data['title'], self.url)
        self.assertTrue('created' in data)
        self.assertTrue('updated' in data)

    def _get_postfix(self):
        return 'test' if self.view_type == 'list' else None

    def _get_ok_args(self):
        return [] if self.view_type == 'list' else [self.publication.id]

    def _get_fail_args(self):
        return [] if self.view_type == 'list' else [self.publication.id + 1]

    def test_view_ok(self):
        response = getattr(self, f'_check_response')(*self._get_ok_args())
        getattr(self, f'_check_{self.view_type}_data')(response)

    def test_view_not_found(self):
        response = getattr(self, f'_check_response')(
            *self._get_fail_args(),
            postfix=self._get_postfix(),
            status=HTTP_STATUS_CODE.NOT_FOUND
        )

        expected_data = {'detail': 'Not found.'}
        data = ujson.loads(response.content)
        self.assertEqual(expected_data, data)


@_publication_api_view_test(models.Category, 'list')
class CategoriesViewTest(_AbstractAPIViewTest):
    pass


@_publication_api_view_test(models.Category, 'detail')
class CategoryViewTest(_AbstractAPIViewTest):
    pass


@_publication_api_view_test(models.Tag, 'list')
class TagsViewTest(_AbstractAPIViewTest):
    pass


@_publication_api_view_test(models.Tag, 'detail')
class TagViewTest(_AbstractAPIViewTest):
    pass
