from django.contrib import admin

# Register your models here.
from .models import Table


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
admin.site.register(Table,MemberAdmin)
  

