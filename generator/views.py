from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

    
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get("Uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("Numbers"):
        characters.extend(list("0123456789"))
    if request.GET.get("Special Character"):
        characters.extend(list("~!`@#$%^&*()_-=/><.,"))
    length=int(request.GET.get('length',10))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html', {"password": thepassword})
    
