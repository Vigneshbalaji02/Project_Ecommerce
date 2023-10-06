from django.contrib import admin
from .models import *

"""
class CatagoryAdmin(admin.ModelAdmin):
    list_display=("Name","Description")
class ProductAdmin(admin.ModelAdmin):
    list_display=("Name","Description")"""

admin.site.register(Catagory)
admin.site.register(Product)
