from django.shortcuts import render
from django.views import generic
from .models import Service


class IndexView(generic.ListView):
    template_name = "sheet/index.html"
    context_object_name = "list_services"

    def get_queryset(self):
        return Service.objects.all()

class DetailServiceView(generic.DetailView):
    model = Service
    template_name = "sheet/detail_service.html"

