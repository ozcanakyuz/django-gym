
{% url 'about' as url %}
    <li class="nav-item {% if request.path == url %}active{% endif %}">
    <a class="nav-link" href="{{ url }}">About</a>
    </li>