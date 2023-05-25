from .models import Profile
from django.forms import ModelForm, TextInput


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'login', 'surname', 'name', 'password')

        widgets ={
            'email': TextInput(attrs={
                'class': "login-field",
                'type': "email",
                'name': "email",
                'id': 'add-form',
                'placeholder': 'Почта'
            }),
            'login': TextInput(attrs={
                'class': "login-field",
                'id': 'add-form',
                'data - max - length': "10",
                'data - min - length': "4",
                'type': "text",
                'data-name': "login",
                'placeholder': 'Логин'
            }),
            'surname': TextInput(attrs={
                'class': "login-field",
                'id': 'add-form',
                'type': "text",
                'data-name': "surname",
                'placeholder': 'Фамилия'
            }),
            'name': TextInput(attrs={
                'class': "login-field",
                'id': 'add-form',
                'type': "text",
                'name': "name",
                'placeholder': 'Имя'
            }),
            'password': TextInput(attrs={
                'class': "login-field",
                'id': "add-form",
                'type': "password",
                'name': "password",
                'placeholder': 'Пароль'
            }),
        }
