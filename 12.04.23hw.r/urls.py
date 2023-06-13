from django.urls import path, include
from jobs.views import JobListCreateView, JobRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('api/jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('api/jobs/<int:pk>/', JobRetrieveUpdateDestroyView.as_view(), name='job-retrieve-update-destroy'),
]
