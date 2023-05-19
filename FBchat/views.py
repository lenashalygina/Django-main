from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chat.models import Message

@login_required
def chat(request):
    messages = Message.objects.order_by('created_at')
    return render(request, 'chat/chat.html', {'messages': messages})

@login_required
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    if message.user == request.user:
        message.delete()
    return redirect('chat')