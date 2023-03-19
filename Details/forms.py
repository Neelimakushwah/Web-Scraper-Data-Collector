from django import forms
from .models import ExtractedData

class ExtractionForm(forms.Form):
    site = forms.CharField(label='Site URL', max_length=255)
    xpath = forms.CharField(label='XPath', max_length=255)

    class Meta:
        model = ExtractedData
        fields = ('site','xpath','data','creation_time')
