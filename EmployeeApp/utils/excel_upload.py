from EmployeeApp.models.employee_model import Employee 
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from EmployeeApp.managers.upload_logs import create_log

# Logical functions

def excel_upload(excel_file):
	
	# Load spreadsheet
	work_book 				= load_workbook(excel_file, data_only=True)
	
	# Getting the active row
	rows 					= work_book.active
	total_rows				= 0
	succesful_rows_passed	= 0

	# Array: specifically to be used for handling duplicate entries
	duplicatedDetectArray = []
	duplicateDetectCount  = 0 

	error_message 		  = ""
	is_error 			  = False

	# Looping through number of individual row in total rows
	for a_row in rows:
		# Taking out the header in the excel file
		if total_rows==0:
			total_rows+=1
			pass
		
		# Getting a single row's values
		else:
			concatenateRowValues = "".replace(' ','')
			
			# Getting values from row in array
			a_row_value_array = []

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
				# Excel date entry validation
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
					error_message	 	= "Invalid input. Salary field expected a number"
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

	# Saving and returning log
	create_log(
		get_records=succesful_rows_passed,
		get_errors=is_error
	)
	

	return [is_error, error_message]
	

	


