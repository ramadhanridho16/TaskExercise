from django.db import models

# Create your models here.


class Motivation(models.Model):
    id = models.CharField(primary_key=True)
    messages = models.CharField(max_length=1000)

    def __str__(self):
        return self.messages


class HomeBanner(models.Model):
    id = models.CharField(primary_key=True)
    messages = models.ForeignKey(
        Motivation, on_delete=models.CASCADE, related_name=motivation)
    media = models.ImageField(
        upload_to='banner/%Y/%m/%d', height_field=None, width_field=None)
