from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import Project, ProjectImageModel


class ProjectImageInline(admin.TabularInline):
    model = ProjectImageModel

@admin.register(Project)
class ProjectAdmin(SortableAdmin):
    list_display = ['name_hu',]
    odering = ('order',)
    inlines = [ProjectImageInline]

