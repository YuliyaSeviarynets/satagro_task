from django.db import models


class ABLine(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=255)
    heading = models.FloatField()
    aPoint_lat = models.FloatField()
    aPoint_lon = models.FloatField()
    bPoint_lat = models.FloatField()
    bPoint_lon = models.FloatField()
    name = models.CharField(max_length=255)
    lastModifiedTime = models.DateTimeField()
    archived = models.BooleanField()

    def __str__(self):
        return self.name
