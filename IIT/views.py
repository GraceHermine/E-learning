# IIT/views.py
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')  # Vue pour la page "about"

def contact(request):
    return render(request, 'contact.html')  # Vue pour la page "contact"

def courses(request):
    return render(request, 'courses.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

