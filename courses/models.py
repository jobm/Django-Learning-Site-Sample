from django.db import models

# Create your models here.
class Course(models.Model):
    ctrated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    descrtiption = models.TextField()

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    descrtiption = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ["order",]

    def __str__(self):
        return self.title
