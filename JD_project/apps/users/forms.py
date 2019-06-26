#
__author__ = 'bob'
__date__ = '2019/6/25 14:17'
from django import forms

from users.models import *


class LoginUserForm(forms.ModelForm):
    login_auth_str = forms.CharField(max_length=100,
                                     widget=forms.PasswordInput,
                                     label='口令')

    class Meta:
        model = LoginUser
        fields = '__all__'


class JdUserForm(forms.ModelForm):
    auth_string = forms.CharField(max_length=100,
                                  widget=forms.PasswordInput,
                                  label='密码')

    class Meta:
        model = JdUser
        fields = '__all__'


class JdShoperForm(forms.ModelForm):
    auth_string = forms.CharField(max_length=100,
                                  widget=forms.PasswordInput,
                                  label='密码')

    class Meta:
        model = JdShopper
        fields = '__all__'
