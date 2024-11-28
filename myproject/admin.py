from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import MyProject, GuestBook

admin.site.register(MyProject)
admin.site.register(GuestBook)