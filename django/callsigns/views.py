from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

# Create Callsigns
def index(request):
    callsigns = callsign.objects.all()
    
    form = callsignForm()
    
    if request.method =='POST':
        form = callsignForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'callsigns':callsigns, 'form':form}    
    return render(request, 'callsigns/list.html', context)

# Update callsigns
def update(request, pk):
    callsigns = callsign.objects.get(id=pk)

    form = callsignForm(instance=callsigns)

    if request.method == 'POST':
        form = callsignForm(request.POST, instance=callsigns)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'callsigns/update.html', context)

# Delete callsign
def delete(request, pk):
    item = callsign.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'callsigns/delete.html', context)