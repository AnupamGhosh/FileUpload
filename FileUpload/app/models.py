"""
Definition of models.
"""

from django.db import models
from django.forms import ModelForm

class File(models.Model):
    def filterName(instance, name):
        return name

    upload = models.FileField('Upload File', upload_to = filterName, null = True)

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['upload']
