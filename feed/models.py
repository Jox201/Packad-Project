from django.db import models

# Create your models here.

class MaintenanceTicket(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    date = models.DateTimeField(auto_now=True)
    # TODO add vars here

    def __str__(self):
        return self.text[0:100]
