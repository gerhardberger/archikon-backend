from django.contrib import admin

from .models import Project, ProjectImageModel


class ProjectImageInline(admin.TabularInline):
    model = ProjectImageModel

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

# admin.site.register(Project)
