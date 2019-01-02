from django.db import models

class User(models.Model):
    name = models.CharField(max_length=256)
    photo = models.FileField(null=True,blank=True)


    def __str__(self):
        return self.name
