from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control item',
                                                                }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'form-control item',
                                                                }))

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control item',
                                                                }))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                                'class': 'form-control item',
                                                                }))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                                'class': 'form-control item',
                                                                }))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                                'class': 'form-control item',
                                                                }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'form-control item',
                                                                }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                'class': 'form-control item',
                                                                }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)