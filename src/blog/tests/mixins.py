from django.contrib.auth import get_user_model
from blog import models


class CreateMixin:
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
