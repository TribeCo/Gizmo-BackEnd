from django.contrib import admin
from .models import *
#---------------------------
@admin.register(ForeignOrder)
class ForeignOrderAdmin(admin.ModelAdmin):
    list_display = ('name','discounted_price','id','created','is_valid','updated')
    search_fields = ['name',]
#---------------------------
@admin.register(ForeignProduct)
class ForeignProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ['name',]

#---------------------------
admin.site.register(DubaiSites)
#---------------------------