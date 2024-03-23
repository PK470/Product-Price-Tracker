from django import forms
from .models import Product

class LinkForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('url', )