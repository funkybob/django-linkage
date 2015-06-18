
from django.contrib.contenttypes import generic
from django.db import models
from django.shortcuts import resolve_url

from taggit.managers import TaggableManager
from polymorphic import PolymorphicModel


class Link(PolymorphicModel):
    title = models.CharField(max_length=1024, blank=True)
    # null=True so it won't conflict with uniqueness
    slug = models.SlugField(max_length=1024,
        blank=True,
        null=True,
        unique=True
    )
    description = models.TextField(blank=True)

    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return u'<{}> {} ({})'.format(
            self.__class__.__name__,
            self.title,
            self.href
        )

    def href(self):
        raise NotImplementedError


class SimpleLink(Link):
    url = models.CharField(max_length=1024)

    def href(self):
        return resolve_url(self.url)


class ObjectTypeLink(Link):
    object_type = models.ForeignKey('contenttypes.ContentType')

    def href(self):
        return self.object_type.model_class().get_list_url()


class ObjectLink(Link):
    object_type = models.ForeignKey('contenttypes.ContentType')
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('object_type', 'object_id')

    def href(self):
        return self.content_object.get_aboslute_url()


##
## Menu
##

class Menu(models.Model):
    '''A menu root'''
    title = models.CharField(max_length=1024, unique=True)
    slug = models.SlugField(max_length=1024, unique=True)


class MenuItem(models.Model):
    '''
    Items on a menu.

    This is a dumbed down nested set structure.  Items are ordered by
    their order field, and the 'level' field can be used to indicate
    now 'nested' they are.
    '''
    menu = models.ForeignKey('Menu', related_name='items')
    level = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    label = models.CharField(max_length=1024, blank=True)
    link = models.ForeignKey('Link', null=True, blank=True)

    class Meta:
        ordering = ('order',)
