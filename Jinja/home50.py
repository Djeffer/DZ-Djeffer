from jinja2 import Template

menu = [
    {'href': '/index', 'link': 'Главная'},
    {'href': '/news', 'link': 'Новости'},
    {'href': '/about', 'link': 'О компании'},
    {'href': '/shop', 'link': 'Магазин'},
    {'href': '/contacts', 'link': 'Контакты'}
]

link = '''<ul>
{% for c in menu -%}
{% if c.link == "Главная" -%}
<li><a href="{{ c['href'] }}" class="active">{{ c['link'] }}</a></li>
{% else -%}
<li><a href="{{ c['href'] }}">{{ c['link'] }}</a></li>
{% endif -%}
{% endfor -%}
</ul>
'''
tm = Template(link)
msg = tm.render(menu=menu)

print(msg)
