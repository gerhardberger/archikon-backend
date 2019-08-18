from django.contrib import admin

from .models import Project, ProjectImageModel


class ProjectImageInline(admin.TabularInline):
    model = ProjectImageModel

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_hu',]
    inlines = [ProjectImageInline]

