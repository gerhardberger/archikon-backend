from django.db import models


class Staff(models.Model):
    name = models.TextField()
    title_hu = models.TextField()
    title_en = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    leader = models.BooleanField(default=False)
    image = models.ImageField(upload_to='staff/')

    def __str__(self):
        return str(self.id)
