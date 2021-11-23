from django.db import models

# Create your models here.
class VideoComment(models.Model):
    videoId = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    likes = models.IntegerField(max_length=100)
    dislikes = models.IntegerField(max_length=100)

class VideoReply(models.Model):
    videoId = models.CharField(max_length=50)
    commentId = models.IntegerField(max_length=50)
    reply = models.CharField(max_length=100)