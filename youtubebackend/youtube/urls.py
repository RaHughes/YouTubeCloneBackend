from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.VideoCommentList.as_view()),
    path('replies/', views.VideoReplyList.as_view())
]