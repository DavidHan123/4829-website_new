from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def sponsors(request):
    return render(request, 'core/sponsors.html')
def sponsor(request):
    return render(request, 'core/sponsor.html') 
def events(request):
    return render(request, 'core/events.html')
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')
