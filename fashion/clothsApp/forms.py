from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SignUp
        fields = '__all__'
