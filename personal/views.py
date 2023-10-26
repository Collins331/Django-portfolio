from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'navbar': 'home'})

def portfolio(request):
    return render(request, 'index.html', {'navbar': 'portfolio'})

def resume(request):
    return render(request, 'resume.html', {'navbar': 'resume'})

def form(request):
    return render(request, 'form.html', {'navbar': 'form'})

def viewdata(request):
    return render(request, 'viewdata.html', {'navbar': 'view'})