from django.shortcuts import render
from .models import VideoComment, VideoReply
from .serializers import VideoCommentSerializer, VideoReplySerializer
from rest_framework.views import APIView
from rest_fromework.response import Response
from rest_framework import status


# Create your views here.
