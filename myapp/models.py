from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    title_web=models.CharField(max_length=200)
    title_body=models.TextField()
    title_auther=models.CharField(max_length=20)
    title_num=models.IntegerField()
    title_date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-title_date',)

    def __unicode__(self):
        return self.title