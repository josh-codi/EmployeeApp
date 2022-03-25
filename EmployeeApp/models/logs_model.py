from django.db import models

class Log(models.Model):
    STATUS_SUCCESS = "Success"
    STATUS_FAILED  = "Failed"

    StatusChoice = [
        (STATUS_SUCCESS, STATUS_SUCCESS),
        (STATUS_FAILED, STATUS_FAILED)
    ]
    timestamps      = models.DateTimeField(auto_now=True)
    records         = models.IntegerField(default=0)
    status          = models.CharField(max_length=50, choices=StatusChoice)
    errors          = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return 'logs'
    
    class Meta:
        ordering = ['-id']

    