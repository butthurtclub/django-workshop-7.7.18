from django.views.generic import TemplateView
from blog import models
from django.shortcuts import get_object_or_404


class PublicationsView(TemplateView):
    template_name = None
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        publications = self.model.objects.all()
        context.update({'publications': publications})

        return context


class PublicationView(TemplateView):
    template_name = None
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.model.__name__.lower()
        publication = get_object_or_404(self.model, pk=kwargs.get(f'{name}_id'))
        context.update({name: publication})

        return context


class IndexView(PublicationsView):
    template_name = 'blog/index.tpl'
    model = models.Category


class TagsView(PublicationsView):
    template_name = 'blog/tags.tpl'
    model = models.Tag


class CategoryView(PublicationView):
    template_name = 'blog/category.tpl'
    model = models.Category


class ArticleView(PublicationView):
    template_name = 'blog/article.tpl'
    model = models.Article


class TagView(PublicationView):
    template_name = 'blog/tag.tpl'
    model = models.Tag
