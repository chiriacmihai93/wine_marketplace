from django.shortcuts import render, redirect
from .forms import WineryForm
from django.contrib.auth.decorators import login_required
from .models.winery import Winery
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

@login_required
def add_winery(request):
    if request.method == 'POST':
        form = WineryForm(request.POST, request.FILES)
        if form.is_valid():
            winery = form.save(commit=False)
            # winery.owner = request.user
            # winery.save()
            return redirect('winery_list')  # să o redirecționezi către pagina cu cramele
    else:
        form = WineryForm()
    return render(request, 'add_winery.html', {'form': form})

def winery_list(request):
    wineries = Winery.objects.filter(approved=True)
    return render(request, 'winery_list.html', {'wineries': wineries})

def approve_winery(request, winery_id):
    winery = get_object_or_404(Winery, pk=winery_id)
    winery.approved = True
    winery.save()
    return HttpResponse("Crama a fost aprobată cu succes!")

def winery_detail(request, winery_id):
    winery = get_object_or_404(Winery, pk=winery_id)
    return render(request, 'winery_detail.html', {'winery': winery})