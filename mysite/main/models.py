from django.db import models
from datetime import date
# Create your models here.
class tutorial(models.Model):
    tutorial_title=models.CharField(max_length=300)
    tutorial_content=models.TextField()
    #django.utils.timezone.now
    tutorial_published=models.DateField("date published",default=date.today())
    def __str__(self):
        return self.tutorial_title
        