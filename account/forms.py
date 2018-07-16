from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(widget=forms.PasswordInput, label='密码')


class RegistrationForm(forms.ModelForm):
    # 在User模型默认字段基础上新增验证密码的表单属性
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两次密码不匹配")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", "photo")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
