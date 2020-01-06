from django.shortcuts import render
from .models import State, CapitalCity

def StateList(request):
    items = State.objects.all()
    return render(request, 'StateCapital.html', {'items':items})
