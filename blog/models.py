from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.title