from django.db import models
from adminsortable.models import SortableMixin


class Project(SortableMixin):
    name_hu = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    location_hu = models.CharField(max_length=100)
    location_en = models.CharField(max_length=100)
    country_hu = models.CharField(max_length=50)
    country_en = models.CharField(max_length=50)
    description_hu = models.TextField()
    description_en = models.TextField()
    year = models.CharField(max_length=50)
    selected = models.BooleanField(default=False)
    listed = models.BooleanField(default=False, verbose_name="Project page")
    category = models.CharField(max_length=100, blank=True)
    thumbnail = models.ImageField(upload_to='projects/', null = True, blank=True)
    order = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name_hu

class ProjectImageModel(models.Model):
    image = models.ImageField(upload_to='projects/', null = True)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(self.id)
