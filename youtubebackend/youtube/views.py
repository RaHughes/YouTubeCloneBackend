from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import VideoComment, VideoReply
from .serializers import VideoCommentSerializer, VideoReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class VideoCommentList(APIView):

    def get(self, request):
        comment = VideoComment.objects.all()
        serializer = VideoCommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class VideoReplyList(APIView):
    def get(self, request):
        comment = VideoReply.objects.all()
        serializer = VideoReplySerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)