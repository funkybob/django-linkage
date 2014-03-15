
from django.contrib import admin
from django.db.models import OneToOneField

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from . import models

class LinkChildAdmin(PolymorphicChildModelAdmin):
    base_model = models.Link

# create child admins
child_models = [
    (rel.field.model, LinkChildAdmin)
    for rel in models.Link._meta.get_all_related_objects()
    if isinstance(rel.field, OneToOneField) and issubclass(rel.field.model, models.Link)
]

class LinkAdmin(PolymorphicParentModelAdmin):
    base_model = models.Link
    list_display = ('title', 'slug', 'href', 'description',)

    child_models = child_models

admin.site.register(models.Link, LinkAdmin)

class MenuItemInline(admin.TabularInline):
    model = models.MenuItem

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)

    inlines = [
        MenuItemInline,
    ]
