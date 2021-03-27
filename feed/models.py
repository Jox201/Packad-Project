from django.db import models

# Create your models here.

class MaintenanceTicket(models.Model):
    #text = models.CharField(max_length=140, blank=False, null=False)
    submit_date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=140, blank=False, null=False)
    description = models.CharField(max_length=140, blank=False, null=False)
    spare_parts = []
    issuer = models.CharField(max_length=40, blank=False, null=False)
    verification_status = False
    status = 0 #0-Open  1-Ongoing   2-Finished  3-Cancelled
    start_date = models.DateTimeField(auto_now=True)
    finish_date = models.DateTimeField(auto_now=True)
    nWorkers = 0
    time_taken = 0.0
    # TODO add vars here

    def __str__(self):
        return self.description[0:100]
