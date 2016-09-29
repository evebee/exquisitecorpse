from django.db import models
from django.utils import timezone
from django.core import validators 


class Post(models.Model):
    text = models.TextField(validators=[validators.MinLengthValidator(20)])
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.text