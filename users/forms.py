from logging import PlaceHolder
from django import contrib, forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from users.models import User

class UserloginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': "Введите имя пользователя"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                        'class': 'form-control',
                                        'placeholder': "Введите ваш пароль"}),
    )
    class meta:
        model = User 
        fields = ['username', 'password']
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше фамилию",
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите имя пользователя",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email *youremail@example.com",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш пароль",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Поддтвердите ваш пароль",
            }
        )
    )
    
        

