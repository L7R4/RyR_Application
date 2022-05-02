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
        response_time=self.request.GET.get("time")
        response_pick_folder = self.request.GET.get("pick_folder")

        today = date.today()
        day = today.day
        month = today.month
        year= today.year

        if response_time == "last_week" and response_pick_folder == "sin_filtros":
            start = date.today()
            end = date.today() - datetime.timedelta(days=7)
            return Service.objects.filter(date__range=[end,start])
        elif response_time == "this_month" and response_pick_folder == "sin_filtros":
            start = date(year,month,1)
            end = date(year,month,day)
            return Service.objects.filter(date__range =[start,end])
        elif response_time =="sin_filtros" and response_pick_folder == "sin_filtros":
            return Service.objects.all()


        elif response_pick_folder =="destiempo" and  response_time == "sin_filtros":
            return Service.objects.filter(date__range =[date(year,month,21), date(year,month,30)])
        elif response_pick_folder =="aTiempo" and  response_time == "sin_filtros":
            return Service.objects.filter(date__range =[date(year,month,1), date(year,month,21)])


        elif response_pick_folder =="destiempo" and  response_time == "last_week":
            return Service.objects.filter(date__range =[date(year,month,21), date(year,month,31)])
        
        else:
            return Service.objects.all()
        

class BillView(generic.ListView):
    template_name = "sheet/bills.html"
    context_object_name = "list_bills"
    # queryset = Service.objects.all()

    def get_queryset(self) :
        response_time=self.request.GET.get("time")
        response_pick_folder = self.request.GET.get("pick_folder")

        today = date.today()
        day = today.day
        month = today.month
        year= today.year

        if response_time == "last_week" and response_pick_folder == "sin_filtros":
            start = date.today()
            end = date.today() - datetime.timedelta(days=7)
            return Service.objects.filter(date__range=[end,start])
        elif response_time == "this_month" and response_pick_folder == "sin_filtros":
            start = date(year,month,1)
            end = date(year,month,day)
            return Service.objects.filter(date__range =[start,end])
        elif response_time =="sin_filtros" and response_pick_folder == "sin_filtros":
            return Service.objects.all()


        elif response_pick_folder =="destiempo" and  response_time == "sin_filtros":
            return Service.objects.filter(date__range =[date(year,month,21), date(year,month,30)])
        elif response_pick_folder =="aTiempo" and  response_time == "sin_filtros":
            return Service.objects.filter(date__range =[date(year,month,1), date(year,month,21)])


        elif response_pick_folder =="destiempo" and  response_time == "last_week":
            return Service.objects.filter(date__range =[date(year,month,21), date(year,month,31)])
        
        else:
            return Service.objects.all()
        

class AddService(generic.ListView):
    template_name = "sheet/add_service.html"
    context_object_name = "asd"

    def get_queryset(self):
        return Service.objects.all()
     
        


    

    
    

