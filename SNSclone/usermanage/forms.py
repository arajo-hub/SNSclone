from django import forms
from usermanage.models import user

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=user
        fields=('username', 'email', 'password',)

class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=user
        fields=('username', 'password',)
