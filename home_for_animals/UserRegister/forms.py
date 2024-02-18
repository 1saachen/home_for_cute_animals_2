from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    email = forms.EmailField(error_messages={
        "required": "邮箱不能为空",
        "invalid": "请输入正确的邮箱格式"
    }, validators=[EmailValidator(message="请输入正确的邮箱格式")])

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, min_length=6, error_messages=
    {"max_length": "长度不能超过16位",
     "min_length": "长度不能小于6位",
     "required": "用户名不能为空"
     })
    password = forms.CharField(max_length=16, min_length=6, error_messages=
    {"max_length": "长度不能超过16位",
     "min_length": "长度不能小于6位",
     "required": "密码不能为空"
     })


class RegisterFrom(forms.Form):
    username = forms.CharField(max_length=16, min_length=6, error_messages=
    {"max_length": "长度不能超过16位",
     "min_length": "长度不能小于6位",
     "required": "用户名不能为空"
     })
    password = forms.CharField(max_length=16, min_length=6, error_messages=
    {"max_length": "长度不能超过16位",
     "min_length": "长度不能小于6位",
     "required": "密码不能为空"
     })
    email = forms.EmailField(error_messages={
        "required": "邮箱不能为空",
        "invalid": "请输入正确的邮箱格式"
    }, validators=[EmailValidator(message="请输入正确的邮箱格式")])






