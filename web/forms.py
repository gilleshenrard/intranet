from django.forms import ModelForm
from api.models import User
from django.forms.fields import TextInput
from django.forms.widgets import Textarea, EmailInput, DateInput, PasswordInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'country', 'phone', 'field', 'occupation', 'birthdate', 'description')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'field': TextInput(attrs={'class': 'form-control'}),
            'occupation': TextInput(attrs={'class': 'form-control'}),
            'birthdate': DateInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }
