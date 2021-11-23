from rest_framework import serializers
from .models import VideoComment, VideoReply

class VideoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoComment
        fields = ['id', 'videoId', 'comment', 'likes', 'dislikes']

class VideoReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoReply
        fields = ['id', 'videoId', 'commentId', 'reply']        