from django import forms
from django.forms import Form, ModelForm

from apps.retirees.models import Retired


class RetiredForm(ModelForm):
    class Meta:
        model = Retired
        fields = ('first_name', 'last_name', 'phone', 'birth_date')


class SearchRetiredForm(Form):
    search = forms.CharField(max_length=50, required=True)
