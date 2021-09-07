from django.contrib import admin
from .models import Books, Categoey

# Register your models here.

admin.site.register(Categoey)
admin.site.register(Books)