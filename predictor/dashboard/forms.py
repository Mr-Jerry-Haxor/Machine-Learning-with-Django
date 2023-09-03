from django import forms
from .models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'mcv', 'alkphos', 'sgpt', 'sgot', 'gammagt', 'drinks']
