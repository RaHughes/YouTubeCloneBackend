from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import VideoComment, VideoReply
from .serializers import VideoCommentSerializer, VideoReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CommentList(APIView):
    
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



class VideoCommentList(APIView):

    def get_object(self, pk):
        try:
            return VideoComment.objects.get(pk=pk)
        except:
            raise status.HTTP_404_NOT_FOUND    

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = VideoCommentSerializer(comment)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class VideoReplyList(APIView):

    def get_object(self, pk):
        try:
            return VideoReply.objects.get(pk=pk)
        except:
            raise status.HTTP_404_NOT_FOUND    

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = VideoReplySerializer(comment)
        return Response(serializer.data)


    def post(self, request):
        serializer = VideoReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)