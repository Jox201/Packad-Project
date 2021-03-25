from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from .models import MaintenanceTicket

class HomePageView(ListView):
    template_name = 'feed/home.html'
    http_method_names = ["get"]
    model = MaintenanceTicket
    context_object_name = "maintenance_tickets"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["MaintenanceTicket"] = MaintenanceTicket.text
    #     return context
    queryset = MaintenanceTicket.objects.all().order_by('-id')[0:30]
    
