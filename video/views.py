from django.shortcuts import render
from .models import Video
from .services import open_file
from django.http import StreamingHttpResponse

# Create your views here.
def VideoView(request, *args, **kwargs):
    template_name = 'video.html'

    video = Video.objects.all()[0]

    context = {
        'video': video
    }
    return render(request, template_name, context)

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response