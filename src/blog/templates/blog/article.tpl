{% extends 'core/base.tpl' %}

{% block content %}
    <h1 class="mt-5">{{ article.title }}</h1>
    <img src="{{ article.image.url }}">
    {{ article.content|safe }}
{% endblock %}