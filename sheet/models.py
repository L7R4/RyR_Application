from turtle import update
from django.db import models

class Service(models.Model):
    company_name = models.CharField(max_length=100)
    date = models.DateField(blank=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    price_per_hour = models.BooleanField()
    price = models.IntegerField(default=0)
    scanned_file = models.FileField(upload_to="sv/images")

    def __str__(self):
        return self.company_name + " " + str(self.date)


class Bill(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    date = models.DateField(blank=False)
    scanned_file = models.FileField(upload_to="bs/images")

    def __str__(self):
        return self.service + " " + str(self.date)
