from django import forms
from django.contrib.auth.models import User

from djangoProject.BookRadar.models import Review


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=64, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=64, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=64, label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'})
        }
        labels = {
            'username': '',
        }
        help_texts = {
            'username': '',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Hasła nie pasują do siebie.')

        return password2


class OpinionAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'comment']
