from django.db import models
from adminsortable.models import SortableMixin


class Staff(SortableMixin):
    name = models.CharField(max_length=40)
    title_hu = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=100)
    leader = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    description_hu = models.TextField(null = True, blank=True)
    description_en = models.TextField(null = True, blank=True)
    image = models.ImageField(upload_to='staff/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
