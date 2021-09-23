from django.db import models
from django.db.models.fields.files import ImageFieldFile


class Empolyee(models.Model):
    position = (('Junior', 'Junior'), ('Mid level',
                                       'Mid level'), ('Senior', 'Senior'))
    name = models.CharField(max_length=300)
    empolyee_id = models.IntegerField()
    citizan_document = models.FileField(upload_to='documents/')
    adress = models.CharField(max_length=300)
    position = models.CharField(
        max_length=30, choices=position, default="Junior")
