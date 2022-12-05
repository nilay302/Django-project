from django.db import models

# Create your models here.
class Tweets(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=False ,default='SOME STRING')
    created = models.DateTimeField(auto_now_add=True)