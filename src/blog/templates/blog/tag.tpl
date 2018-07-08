{% extends 'core/base.tpl' %}
{% import 'blog/macros.tpl' as macros %}
{% block content %}
    <h1 class="mt-5">{{ tag.title }}</h1>
{% endblock %}