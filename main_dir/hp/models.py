from django.db import models

# Create your models here.

from django.db import models
#class to extrat headline of news articles
class Extract_Headline(models.Model):
  title = models.CharField(max_length=300)
  # image = models.URLField(null=True, blank=True)
  url = models.TextField()

  def __str__(self):
    return self.title
