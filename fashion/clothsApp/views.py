from django.shortcuts import render
from .forms import SignUpForm


# Create your views here.

def HomeView(request):
    template_name = 'clothsApp/Home.html'
    context = {}
    return render(request, template_name, context)


def MensView(request):
    template_name = 'clothsApp/Mens.html'
    context = {}
    return render(request, template_name, context)


def LadiesView(request):
    template_name = 'clothsApp/Ladies.html'
    context = {}
    return render(request, template_name, context)


def KidsView(request):
    template_name = 'clothsApp/Kids.html'
    context = {}
    return render(request, template_name, context)


def Accessories(request):
    template_name = 'clothsApp/Accessories.html'
    context = {}
    return render(request, template_name, context)


def SignUpView(request):
    form = SignUpForm()
    template_name = 'clothsApp/SignUp.html'
    context = {'form': form}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template_name, context)
