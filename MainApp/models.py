from django.db import models


class Colour(models.Model):
    name = models.CharField(max_length=32)


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(max_length=100, default='Base description')
    colours = models.ManyToManyField(to=Colour)

