from django.db import models


# Create your models here.
class GPSPoint(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lat} {self.lon} {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']


class Device(models.Model):
    name = models.CharField(max_length=255)
    gps = models.ForeignKey(GPSPoint, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class TrackedUser(models.Model):
    name = models.CharField(max_length=255)
    devices = models.ManyToManyField(Device)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
