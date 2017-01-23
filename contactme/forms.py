from django import forms
from django.forms import ModelForm

from .models import Feedback


class ContactForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['create_date']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'field_class'