from django.urls import path
from chat.views import chat , delete_message

urlpatterns = [
    path('chat/', chat, name='chat'),
    path('delete_message/<int:message_id>/', delete_message, name='delete_message'),
]
