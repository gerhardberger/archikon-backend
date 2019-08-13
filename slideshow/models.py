from django.db import models


class SlideShow(models.Model):
    image = models.ImageField(upload_to='slideshows/')

    def __str__(self):
        return str(self.id)
