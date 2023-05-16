#from django.contrib.auth.models import User
from Eapp.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Eapp.models import CourseCategory


class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Password"
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter confirm Password"
		}))
	class Meta:
		model = User
		#fields = '__all__'
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username"
			})
		}

class Crcty(forms.ModelForm):
	class Meta:
		model = CourseCategory
		fields = ["ctitle"]
		widgets = {
		"ctitle":forms.TextInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter Course",
		})
		}

class pfupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email","age","gender","mobile","pfimge"]
		widgets = {
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter First name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Last name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Email id",
			}),
		"age":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Age",
			}),
		"mobile":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Mobile number",
			}),
		}
class ChPwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter old Password",}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Enter new Password",}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Confirm new Password",}))
	class Meta:
		model = User
		fields = "__all__"