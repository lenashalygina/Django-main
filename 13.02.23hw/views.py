import os
import cv2
import dlib
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Video


# Загрузка видео
class VideoUploadView(View):
    def post(self, request):
        video_file = request.FILES.get('video_file')
        video = Video(video_file=video_file)
        video.save()
        return HttpResponse('Video uploaded successfully!')


# Обработка видео и распознавание лиц
class VideoProcessView(View):
    def get(self, request, video_id):
        video = get_object_or_404(Video, id=video_id)

        video_path = video.video_file.path
        faces_dir = os.path.join('static', 'faces', str(video_id))
        os.makedirs(faces_dir, exist_ok=True)
        video.processed = True
        video.save()
        return HttpResponse('Video processed successfully!')


class FaceListView(View):
    def get(self, request, video_id):
        video = get_object_or_404(Video, id=video_id)
        faces_dir = os.path.join('faces', str(video_id))
        face_images = [f for f in os.listdir(faces_dir) if os.path.isfile(os.path.join(faces_dir, f))]
        return HttpResponse(f'Found faces: {len(face_images)}')

