from django.shortcuts import render
from pupa.models import *

# Create your views here.
def pupa(request):
    if request.method == "GET":
        updates = Update.objects.all()
        context = {
            "updates":updates
        }
    return render(request, 'pupa.html', context)