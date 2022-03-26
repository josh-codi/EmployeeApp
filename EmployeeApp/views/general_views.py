# Django imports
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
# Local app imports 
from EmployeeApp.utils.excel_upload import excel_upload
from EmployeeApp.models.employee_model import Employee
from EmployeeApp.models.logs_model import Log
from EmployeeApp.forms import EmployeeForm
from EmployeeApp.managers.upload_logs import create_log



# Create your views here.
@login_required
def employee_list(request):
	employees = Employee.objects.all()
	context = {
		"employees": employees
	}
	return render(request, 'employee_list.html', context)



@login_required
def add_employee(request):
	form = EmployeeForm()
	if request.method == "POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			create_log(
				get_records=1,
			)
			messages.success(request, 'SUCCESSFUL, You added a new Employee !')
		else:
			create_log(
				get_records=0,
				get_errors=messages.error
			)
			messages.error(request, "UNSUCCESSFUL, Couldn't add Employee !")

	context={
		"form":form
	}
	return render(request, 'addEmployee.html', context)



@login_required
def add_excel(request):
	if request.method == "POST":
		excel_file     			= request.FILES.get("employee_excel_file")
		# Getting filename and extension	
		file_name, extension 	= os.path.splitext(excel_file.name)
		if '.xlsx' == extension:
			upload_info = excel_upload(excel_file)
			# Checking if any error occured
			if upload_info[0]==True:
				messages.error(request, upload_info[1])

			# Valid file
			else:
				messages.success(request, "Employee Data uploaded successfully")
						
		# If file wasn't a '.xlsx'
		else:
			messages.error(request, "Invalid file upload, please upload an excel file")
			
	return render(request, 'addExcel.html')




@login_required
def logs(request):
	logs = Log.objects.all()
	context={
		"logs":logs
	}
	return render(request, 'logs.html', context)


