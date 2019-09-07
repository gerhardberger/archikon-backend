from django.db import models
from adminsortable.models import SortableMixin


class SlideShow(SortableMixin):
    url = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='slideshows/')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.url
