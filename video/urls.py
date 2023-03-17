from django.urls import path
from .views import VideoView, get_streaming_video

urlpatterns = [
    path('', VideoView, name="video"),
    path('stream/<int:pk>/', get_streaming_video, name='stream'),
]

