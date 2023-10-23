from django.db import models


# Create your models here.
class MTS(models.Model):
    timestamp = models.DateTimeField("timestamp")
    U3_HNC10CT111 = models.FloatField("U3_HNC10CT111")
    U3_HNC10CT121 = models.FloatField("U3_HNC10CT121")
    U3_HNC10CT131 = models.FloatField("U3_HNC10CT131")
