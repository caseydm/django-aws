from django import forms
from django.forms import ModelForm
from .models import ContactForm


class ContactView(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'topic', 'message']
