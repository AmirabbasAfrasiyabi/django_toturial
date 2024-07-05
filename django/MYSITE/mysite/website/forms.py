
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    subject = forms.CharField(max_length=255)
    massage = forms.CharField(widget=forms.Textarea)