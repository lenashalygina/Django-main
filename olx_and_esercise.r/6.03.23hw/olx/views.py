from django.shortcuts import render, redirect
from .models import Announcement
from .forms import AnnouncementForm

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    return render(request, 'announcements/announcement_detail.html', {'announcement': announcement})

def announcement_create(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/announcement_form.html', {'form': form})

def announcement_edit(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            announcement = form.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcements/announcement_form.html', {'form': form})
