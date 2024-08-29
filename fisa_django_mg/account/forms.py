from django import forms

class LoginForm(forms.Form):
    # input을 2개 받음
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  # text를 받되 ****처리