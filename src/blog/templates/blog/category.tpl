{% extends 'core/base.tpl' %}
{% import 'blog/macros.tpl' as macros %}
{% block content %}
    <h1 class="mt-5">{{ category.title }}</h1>
    {{ macros.publications_list('article', category.articles.all()) }}
{% endblock %}