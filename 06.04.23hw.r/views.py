from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import ProfileForm


@login_required
def profile_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})
