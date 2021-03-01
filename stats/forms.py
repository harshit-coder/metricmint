from django.forms import ModelForm
from django import forms
from stats.models import *


class searchform(forms.ModelForm):
    class Meta:
        model = searchenter
        fields = ['searc']
        labels ={'searc':'search anything:'}
        searc = forms.CharField(max_length=900,required=True)
        widgets={
        'searc':forms.TextInput(attrs={'class':'form-control form-control-lg form-control-borderless','placeholder':"search anything"})

                }