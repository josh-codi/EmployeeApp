from EmployeeApp.models.employee_model import Employee # Data will be saved to this model
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

from EmployeeApp.managers.upload_logs import create_log # Creating a log after a call to this function

# Logical functions

def excel_upload(excel_file):
	
	# Load spreadsheet
	work_book 				= load_workbook(excel_file, data_only=True) #Loading excel file but the space with data only 
	
	# Getting active rows
	rows 					= work_book.active # Creates an array of which each row is saved as an element
	total_rows				= 0	# Counter for iterations from row one(1) to the last row
	succesful_rows_passed	= 0 

	# Array to handle duplicate entries
	duplicatedDetectArray = []
	duplicateDetectCount  = 0 

	error_message 		  = ""
	is_error 			  = False

	# Iterating all the rows
	for a_row in rows:
		# Kicking off the header of the table
		if total_rows==0:
			total_rows+=1
			pass
		
		# Getting each single row's values
		else:
			concatenateRowValues = "".replace(' ','') # first_namemiddle_namepositionsalarysupervisorsdate_of_employmentdate_of_graduationcode
			
			# Getting values from row in array
			a_row_value_array = [] # ordered in the form ===  first_name | middle_name | position | salary | supervisors | date_of_employment | date_of_graduation | code

			# a_row has it's elements as each of it's columns
			for a_row_value in a_row:
				# appending employee a_row_value_array
				a_row_value_array.append(a_row_value.value)
				# Concatenating
				concatenateRowValues+= str(a_row_value.value)
							
			# Checking and manipulating duplicate row data
			exists = concatenateRowValues in duplicatedDetectArray
			if exists ==True:
				duplicateDetectCount+=1
				pass
			# Creating employee
			else:
				first_name 				= a_row_value_array[0]
				middle_name 			= a_row_value_array[1]
				
				# Date entry validation
				try:
					if '"' not in a_row_value_array[2] and '"' not in a_row_value_array[3]:
						is_error 			= True
						error_message 		= "Please round your datetimes in quotation marks"
					else:
						date_of_graduation		= a_row_value_array[2].strip('"')
						date_of_graduation 		= date_of_graduation.strip("'")

						date_of_employment 		= a_row_value_array[3].strip('"')
						date_of_employment 		= date_of_employment.strip("'")
					
				except:
					is_error 			= False
					error_message		= ""
					break


				position 				= a_row_value_array[4]

				try:
					salary 				= int(a_row_value_array[5])
				except:
					is_error 			= True
					error_message	 	= "Salary field expects a number"
					break

				
				# Saving employee into database
				try:
					employee 				= Employee(
												first_name=first_name, middle_name=middle_name,
												date_of_graduation=date_of_graduation, 
												date_of_employment=date_of_employment, position=position,
												salary=salary)
					employee.save()
					succesful_rows_passed+=1
					duplicatedDetectArray.append(concatenateRowValues)

				except Exception as e:
					is_error 		= True
					error_message 	= str(e)
					break

							
			total_rows+=1

	# Saving and returning log to the logs table
	create_log(
		get_records=succesful_rows_passed,
		get_errors=is_error
	)
	

	return [is_error, error_message]
	

	


