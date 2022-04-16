from django.urls import path
from . import views

app_name="hojas"
urlpatterns = [
    path('',views.index, name="index"),
    path('services_lists/',views.ServiceView.as_view(), name="services_lists")
]