from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
