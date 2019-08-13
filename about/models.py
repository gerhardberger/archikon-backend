from django.db import models


class About(models.Model):
    info_hu = models.TextField()
    info_en = models.TextField()

    def __str__(self):
        return str(self.id)
