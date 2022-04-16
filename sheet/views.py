from django.shortcuts import render
from django.views import View, generic
from .models import Service


def index(request):
    return render(request,"sheet/index.html")
    

class ServiceView(generic.ListView):
    template_name = "sheet/services.html"
    context_object_name = "list_services"

    def get_queryset(self):
        return Service.objects.all()

