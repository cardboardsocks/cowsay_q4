from django import forms
from cowsays.models import Cowsays


class AddCowsay(forms.Form):
    cowsays = forms.CharField(max_length=80) 