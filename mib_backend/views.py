from django.shortcuts import render
from pupa.models import *

def home(request):
    if request.method == "GET":
        context = {
            'team_members': TeamMember.objects.all()
        }
        print(context)
    return render(request, 'home.html', context=context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return render(request, 'contact.html')

def gallery(request):
    if request.method == "GET":
        gallery = Gallery.objects.all()
        context = {
            "photos":gallery
        }
    return render(request, 'gallery.html', context)

    