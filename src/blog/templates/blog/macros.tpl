{% macro publications_list(name, publications) -%}
    <ul>
        {% set url_name = 'blog:' + name %}
        {% for publication in publications %}
            <li><a href="{{ url(url_name, publication.id) }}">{{ publication.title }}</a></li>
        {% endfor %}
    </ul>
{%- endmacro %}