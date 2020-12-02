from django import forms

class loginForm(forms.Form):
    loginName = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)
    Symbol = forms.CharField()