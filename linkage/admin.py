
from django.contrib import admin
from django.db.models import OneToOneField

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from . import models
from . import forms

class LinkChildAdmin(PolymorphicChildModelAdmin):
    base_model = models.Link


class ObjectTypeLinkAdmin(LinkChildAdmin):
    form_class = forms.ObjectTypeLinkForm


class ObjectLinkAdmin(LinkChildAdmin):
    form_class = forms.ObjectLinkForm


class LinkAdmin(PolymorphicParentModelAdmin):
    base_model = models.Link
    list_display = ('title', 'slug', 'href', 'description',)

    child_models = (
        #(models.Link, LinkChildAdmin),
        (models.SimpleLink, LinkChildAdmin),
        (models.ObjectTypeLink, ObjectTypeLinkAdmin),
        (models.ObjectLink, ObjectLinkAdmin),
    )

admin.site.register(models.Link, LinkAdmin)

class MenuItemInline(admin.TabularInline):
    model = models.MenuItem

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)

    inlines = [
        MenuItemInline,
    ]
