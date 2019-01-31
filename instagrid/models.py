from django.db import models
from pyuploadcare.dj.models import ImageField


class Post(models.Model):
    photo = ImageField(blank=True, manual_crop="")