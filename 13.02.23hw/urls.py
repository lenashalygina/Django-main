from django.urls import path
from . import views

app_name = 'video_processing_app'

urlpatterns = [
    path('upload/', views.VideoUploadView.as_view(), name='video_upload'),
    path('process/<int:video_id>/', views.VideoProcessView.as_view(), name='video_process'),
    path('faces/<int:video_id>/', views.FaceListView.as_view(), name='face_list'),
]