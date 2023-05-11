from django.urls import path
from views import fetch_jsonplaceholder_data

urlpatterns = [
    path('fetch-data/', fetch_jsonplaceholder_data, name='fetch_jsonplaceholder_data'),
]
