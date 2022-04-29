from EmployeeApp.models.logs_model import Log

def create_log(get_records, get_errors=None):
	# Handling failed records
	if get_errors:
		log = Log.objects.create(
			records= get_records,
			status = Log.STATUS_FAILED,
			errors = get_errors   
		)
	# Handling success records
	else:
		log = Log.objects.create(
			records= get_records,
			status=Log.STATUS_SUCCESS
		)
