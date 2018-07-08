<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>{% block title %}{% endblock %}</title>
        <link href="{{STATIC_URL}}bootstrap.min.css" rel="stylesheet">
        <link href="{{STATIC_URL}}sticky.css" rel="stylesheet">
    </head>
    <body>
        {% include 'core/header.tpl' %}
        <main role="main" class="container">{% block content %}{% endblock %}</main>
        {% include 'core/footer.tpl' %}
    </body>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="{{STATIC_URL}}bootstrap.min.js"></script>
</html>
