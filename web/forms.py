from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.forms.fields import TextInput
from django.forms.widgets import Textarea, EmailInput, DateInput


class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        exclude = ['username', 'password', 'groups', 'is_active', 'id', 'last_login', 'user_permissions', 'is_staff', 'is_superuser', 'date_joined']
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
