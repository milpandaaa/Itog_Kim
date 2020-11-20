from django.contrib import admin
from .models import *
models = [Book, Reader, Card]
admin.site.register(models)
# Register your models here.
