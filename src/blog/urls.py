from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^tags/$', views.TagsView.as_view(), name='tags'),
    re_path(
        r'^category/(?P<category_id>[\d]+)/$',
        views.CategoryView.as_view(),
        name='category'
    ),
    re_path(
        r'^article/(?P<article_id>[\d]+)/$',
        views.ArticleView.as_view(),
        name='article'
    ),
    re_path(
        r'^tags/(?P<tag_id>[\d]+)/$',
        views.TagView.as_view(),
        name='tag'
    )
]