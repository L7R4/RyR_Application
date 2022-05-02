from django.urls import path
from . import views

app_name="hojas"
urlpatterns = [
    path('',views.index, name="index"),
    path('services_lists/',views.ServiceView.as_view(), name="services_lists"),
    path('bills_lists/', views.BillView.as_view(), name ="bills_lists"),
    path("add_service/", views.AddService.as_view(), name="add_service")
]