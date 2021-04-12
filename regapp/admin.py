from django.contrib import admin
from regapp.models import student


# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display = ('name', 'fathername', 'email', 'contact', 'password1', 'password2')


admin.site.register(student, studentadmin)
