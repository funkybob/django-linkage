from __future__ import absolute_import

from contextlib import contextmanager

from linkage.models import Link, Menu

from django.db.models import Q
from django import template
from django.template.loader import get_template

register = template.Library()


@contextmanager
def extra_context(context, extra, **kwargs):
    '''Helper for adding extra context, and cleaning up after ourselves.'''
    extra.update(kwargs)
    context.update(extra)
    yield context
    context.pop()


@register.assignment_tag
def get_menu(name):
    try:
        return Menu.objects.select_related('items').get(
            Q(title=name) | Q(slug=name)
        )
    except Menu.DoesNotExist:
        return None


@register.assignment_tag
def load_links_with(*tags):
    '''Load a list of links sharing all tags

    {% load_links_with 'foo' as foo_links %}
    '''
    qs = Link.objects.all()
    for tag in tags:
        qs = qs.filter(tags__name=tag)
    return qs


@register.simple_tag(takes_context=True, name='link')
def do_link(context, name, **kwargs):
    try:
        link = Link.objects.select_related('items').get(
            Q(title=name) | Q(slug=name)
        )
    except Link.DoesNotExist:
        return ''

    template_name = kwargs.get('template', 'linkage/link.html')
    template = get_template(template_name)

    with extra_context(context, kwargs, link=link):
        return template.render(context)


@register.simple_tag(takes_context=True, name='menu')
def do_menu(context, name, **kwargs):
    try:
        menu = Menu.objects.select_related('items').get(
            Q(title=name) | Q(slug=name)
        )
    except Menu.DoesNotExist:
        return ''

    template_name = kwargs.get('template_name', 'linkage/menu.html')
    template = get_template(template_name)

    with extra_context(context, kwargs, menu=menu):
        return template.render(context)
