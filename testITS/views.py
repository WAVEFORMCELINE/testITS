from django.http import HttpResponse
from .generate_video import generate_video


def generate_video_view(request, text):
    video_data = generate_video(text)  # предположим, это массив байтов

    response = HttpResponse(video_data, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=video.mp4'

    return response