from django.contrib import admin
from .models import *
from django.db import models

class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Student Profile', {'fields': ('first_name','last_name','email','residence_address',)}),
        ('School Details', {'fields': ('school','standard','roll_no','fees',)}),
        ('Permission', {'fields': ('enabled', )}),
    )

    ordering = ('-created_date',)
    list_display = ('first_name','last_name','email','residence_address','standard','school','roll_no','fees','enabled','created_date','modified_date',)
    search_fields = ('first_name','last_name','roll_no',)
    list_filter = ('enabled','first_name','last_name', )
	
class SchoolAdmin(admin.ModelAdmin):
    fieldsets = (
        ('School Profile', {'fields': ('name', 'address','rating','email','contact_no','website',)}),
        ('Permission', {'fields': ('enabled', )}),
    )
    list_display = ('name', 'address','rating','email','contact_no','website','enabled','created_date','modified_date',)
    search_fields = ('name',)
    ordering = ('-created_date',)
    list_display_links = ('name',)
    list_filter = ('enabled','name','email',)

admin.site.register(Student ,StudentAdmin)
admin.site.register(School, SchoolAdmin)
