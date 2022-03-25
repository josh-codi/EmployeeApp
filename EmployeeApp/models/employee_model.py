from django.db import models
from EmployeeApp.utils.generate_code import generate_code
# Create your models here.

class Employee(models.Model):
    first_name      = models.CharField(max_length=100)
    middle_name     = models.CharField(max_length=100)
    date_of_graduation= models.DateField(blank=True)
    date_of_employment= models.DateField(blank=True)
    position        = models.CharField(max_length=100)
    salary          = models.IntegerField(default=0)
    supervisors     = models.ManyToManyField('Employee', blank=True)
    employee_code   = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.middle_name}'

    class Meta:
        ordering = ['-id']

        
    def save(self, *args, **kwargs):
        first_name_init = self.first_name[0]
        middle_name_init = self.middle_name[0]
        rand_num         = generate_code()
        code        = first_name_init+middle_name_init+'-'+rand_num
        self.employee_code  = code  
        super().save(*args, **kwargs)