from django.db import models

# Create your models here.
class Course(models.Model):
    ctrated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    descrtiption = models.TextField()

    def __str__(self):
        return self.title
