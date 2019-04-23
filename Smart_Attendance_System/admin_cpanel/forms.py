from django import forms
from . import models


class UploadFile(forms.ModelForm):
    class Meta:
        model = models.UploadFile
        fields = ['file']
