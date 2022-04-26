from http.client import HTTPResponse
from msilib.schema import ServiceInstall
from django.http import Http404, HttpResponse,HttpRequest,QueryDict
from django.shortcuts import render
from django.views import View, generic
from .models import Service
import datetime
from datetime import date


def index(request):
    return render(request,"sheet/index.html")
    

class ServiceView(generic.ListView):
    template_name = "sheet/services.html"
    context_object_name = "list_services"
    # queryset = Service.objects.all()

    def get_queryset(self) :
        nashe=self.request.GET.get("time")
        if nashe == "esta_semana":
            start = date.today()
            end = date.today() - datetime.timedelta(days=6)
            print(start)
            print(end)
            print(Service.date)
            return Service.objects.filter(date__gte =end)
        else:
            return Service.objects.all()


    

    
    

