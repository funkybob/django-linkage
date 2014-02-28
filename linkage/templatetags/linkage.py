
from linkage import models

from django.db.models import Q
from django import template

register = template.Library()

@register.filter
def get_menu(name):
    return models.Menu.objects.select_related('items').get(
        Q(title=name) | Q(slug=name)
    )
