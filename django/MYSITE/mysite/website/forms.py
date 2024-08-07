from django import forms
from website.models import Contact, NewsLetter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'  # Corrected 'field' to 'fields'

class NewsletterForm(forms.ModelForm):  # Corrected 'Modelform' to 'ModelForm'
    class Meta:
        model = NewsLetter
        fields = '__all__'  # Corrected 'field' to 'fields'
