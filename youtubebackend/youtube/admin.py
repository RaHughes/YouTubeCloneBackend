from django.contrib import admin
from .models import VideoComment, VideoReply

# Register your models here.
admin.site.register(VideoComment)
admin.site.register(VideoReply)