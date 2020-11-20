from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    year = models.IntegerField()
    theme = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    translate = models.CharField(max_length=50)


class Reader(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)


class Card(models.Model):
    book = models.IntegerField(default=None)
    reader = models.IntegerField(default=None)
    date = models.DateTimeField(auto_now_add=True)