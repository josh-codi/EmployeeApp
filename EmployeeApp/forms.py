from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from EmployeeApp.models.employee_model import Employee

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, required=True,
				widget=forms.TextInput(attrs={
					"placeholder":"Username",
					 "id":"username",
					 "class":"form-control",
					 "placeholder":"Username",
					 "autofocus":""
				})
				)
	
	password = forms.CharField(max_length=500,
						required=True,
						widget=forms.PasswordInput(attrs={
							"id":"inputPassword", 
							"class":"form-control",
							"placeholder":"Password"
						})
						)
	
	class Meta:
		model = User,
		fields = ["username","password"]



class EmployeeForm(ModelForm):
	first_name = forms.CharField(max_length=100, required=True,
				widget=forms.TextInput(attrs={
					"name":"firstName",
					"class":"form-control",
					"id":"firstName"
				})
				)

	middle_name = forms.CharField(max_length=100, required=True,
				widget=forms.TextInput(attrs={
					"name":"middleName",
					"class":"form-control",
					"id":"middleName"
				})
				)

	position = forms.CharField(max_length=100, required=True,
				widget=forms.TextInput(attrs={
					"name":"position",
					"class":"form-control",
					"id":"position"
				})
				)

	salary = forms.CharField(max_length=100, required=True,
				widget=forms.NumberInput(attrs={
					"name":"salary",
					"class":"form-control",
					"id":"salary"
				})
				)


	date_of_employment = forms.CharField(max_length=100, required=True,
				widget=forms.DateInput(attrs={
					"name":"dateOfEmployment",
					"class":"form-control",
					"id":"dateOfEmployment"
				})
				)

	date_of_graduation = forms.CharField(max_length=100, required=True,
				widget=forms.DateInput(attrs={
					"name":"dateOfGraduation",
					"class":"form-control",
					"id":"dateOfGraduation"
				})
				)
	supervisors = forms.ModelMultipleChoiceField(
		queryset=Employee.objects.all()
		)
	
	class Meta:
		model = Employee
		fields = ["first_name", "middle_name", "position", "salary", "date_of_employment", "date_of_graduation", "supervisors"]