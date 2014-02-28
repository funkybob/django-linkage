
from contextlib import contextmanager

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

@contextmanager
def extra_context(context, extra):
    '''Temporarily add some context, and clean up after ourselves.'''
    context.update(extra)
    yield
    context.pop()

@register.simple_tag(takes_context=True)
def link(context, slug, *args, **kwargs):
    '''Embed a link'''
    # Find the link by slug
    try:
        link = Link.objects.get(slug=slug)
    except Link.DoesNotExist:
        return ''

    if 'template' in kwargs:
        tmpl = get_template(kwargs.pop('template'))
    else:
        tmpl = template.Template('<a href="{{ link.url }}>{{ link.title }}</a>')
    with extra_context(context, kwargs, link=link):
        return tmpl.render(context)
