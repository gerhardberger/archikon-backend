from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import Staff

@admin.register(Staff)
class StaffAdmin(SortableAdmin):
    list_display = ['name',]

