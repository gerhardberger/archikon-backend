from django.db import models


class Contact(models.Model):
    title_hu = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    info_hu = models.TextField()
    info_en = models.TextField()

    def __str__(self):
        return str(self.id)
