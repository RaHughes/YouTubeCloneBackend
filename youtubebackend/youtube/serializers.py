from rest_framework import serializers
from .models import VideoComment, VideoReply

class VideoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoComment
        fields = ['id', 'videoId', 'commentId', 'likes', 'dislikes']

class VideoReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoReply
        field = ['id', 'videoId', 'commentId', 'reply']        