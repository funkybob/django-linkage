
from django.contrib.contenttypes.models import ContentType
from django import forms

from . import models

# Models we can find a list page for
LISTABLE_OBJECTS = ContentType.objects.get_for_models(*[
    model
    for app, model in models.get_models()
    if callable(getattr(model, 'get_list_url', None))
])


# The list of models we know how to get a url for
LINKABLE_OBJECTS = ContentType.objects.get_for_models(*[
    model
    for app, model in models.get_models()
    if callable(getattr(model, 'get_absolute_url', None))
])


class ObjectTypeLinkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ObjectTypeLinkForm, self).__init__(*args, **kwargs)
        self.fields['object_type'].queryset = LISTABLE_OBJECTS

    class Meta:
        model = models.ObjectTypeLink


class ObjectLinkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ObjectLinkForm, self).__init__(*args, **kwargs)
        self.fields['object_type'].queryset = LINKABLE_OBJECTS

    class Meta:
        model = models.ObjectLink
