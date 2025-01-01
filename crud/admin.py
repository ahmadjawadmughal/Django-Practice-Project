from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # list_display = ["name", "age", "email"]
    search_fields = ["name", "email"]
    