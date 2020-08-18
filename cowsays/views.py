from django.shortcuts import render, HttpResponseRedirect, reverse
from cowsays.forms import AddCowsay
from cowsays import models
import subprocess
# Create your views here.

def cowsaid(request):
    if request.method == "POST":
        form = AddCowsay(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cowsays = data.get('cowsays')
            models.Cowsays.objects.create(cowsays = cowsays)
            cow_process = subprocess.run(f'cowsay "{cowsays}"', capture_output=True, shell=True)
            cow_picture = cow_process.stdout.decode('utf-8')
            form = AddCowsay()
            return render(request, 'index.html', {'cowsaid': cow_picture, 'form': form, "Welcome": "What would you like the cow to say?"})
    form = AddCowsay()
    return render(request, "index.html", {"form": form, "Welcome": "What would you like the cow to say?"})


def cowsay_history(request):
    cowsaid = models.Cowsays.objects.all().order_by('-id')[:10]
    return render(request, "history.html", {"cowsays": cowsaid})