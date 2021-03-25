from django.contrib import admin
from .models import MaintenanceTicket

class MaintenanceTicketAdmin(admin.ModelAdmin):
    pass

admin.site.register(MaintenanceTicket, MaintenanceTicketAdmin)
