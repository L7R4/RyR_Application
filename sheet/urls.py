from django.urls import path
from . import views

app_name="hojas"
urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('<int:pk>/',views.DetailServiceView.as_view(), name="service_detail")
]