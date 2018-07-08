{% extends 'core/base.tpl' %}
{% import 'blog/macros.tpl' as macros %}
{% block content %}
    <h1 class="mt-5">Теги:</h1>
    {{ macros.publications_list('tag', publications) }}
{% endblock %}