#
__author__ = 'bob'
__date__ = '2019/6/25 14:17'
from django import forms

from users.models import *


class JdShopperForm(forms.ModelForm):
    m_pwd = forms.CharField(max_length=100,
                            widget=forms.PasswordInput,
                            label='口令')

    class Meta:
        model = JdShopper
        fields = '__all__'



