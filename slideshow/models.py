from django.db import models


class SlideShow(models.Model):
    url = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='slideshows/')

    def __str__(self):
        return str(self.id)
