from django.http import HttpResponse
from django.shortcuts import render
from .generate_video import generate_video
from logs.models import QueryLog

def generate_video_view(request, text):
    video_data = generate_video(text)  # предположим, это массив байтов
    response = HttpResponse(video_data, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=video.mp4'
    return response

def generate_video_page(request):
    return render(request, 'generate-video.html')


def logs_view(request):
    query_logs = QueryLog.objects.all()
    return render(request, 'logs.html', {'query_logs': query_logs})