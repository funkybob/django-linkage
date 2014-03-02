
from linkage import models

from django.db.models import Q
from django import template

register = template.Library()


@register.filter
def get_menu(name):
    return models.Menu.objects.select_related('items').get(
        Q(title=name) | Q(slug=name)
    )


@register.assignment_tag
def load_links_with(*tags):
    '''Load a list of links sharing all tags

    {% load_links_with 'foo' as foo_links %}
    '''
    qs = models.Menu.objects.all()
    for tag in tags:
        qs = qs.filter(tags__name=tag)
    return qs


@register.inclusion_tag(template_name="linkage/menu.html")
def menu(menu_name):
    menu = models.Menu.objects.select_related('items').get(
        Q(title=name) | Q(slug=name)
    )
    return {'menu': menu}

