from django.urls import path
from . import views

urlpatters = [
    path('comments/', views.VideoCommentList.as_view()),
    path('replies/', views.VideoReplyList.as_view())
]