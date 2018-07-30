from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    TITLE_ITEM = (('F','flight'),('B','b737'), ('P','python'), ('R','redwine'),)
    title=models.CharField(max_length=200)
    title_web=models.URLField(max_length=200)
    title_body=models.TextField()
    title_auther=models.CharField(max_length=20)
    title_num=models.IntegerField()
    title_date=models.DateTimeField(default=timezone.now)
    title_item=models.CharField(max_length=20, default='flight',choices=TITLE_ITEM)


    class Meta:
        ordering=('-title_date',)

    def __str__(self):
        return self.title
