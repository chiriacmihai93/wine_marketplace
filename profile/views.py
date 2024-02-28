from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models.profile import Profile
from .forms import ProfileForm


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'profile.html', {'form': form})
