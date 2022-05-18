from django import forms
from . import models


class TVShowForm(forms.ModelForm):
    class Meta:
        model = models.Shows
        fields = "__all__"
