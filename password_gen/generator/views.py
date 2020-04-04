from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random

def home(request):
    return render(request, "generator/home.html", {"password": "sadasgert4tggsdf"})

def password(request):

    characters = list("qwertyuiopasdfghjklzxcvbnm")

    if request.GET.get('uppercase'):
        characters.extend(list("QWERTYUIOPLKJHGFDSAZXCVBNM"))

    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_-+=<>>?|"))

    if request.GET.get('numbers'):
        characters.extend(list("12345671223253465437568706763523534566546890"))

    lenght = int(request.GET.get('length', 12))
    thepassword = ""

    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {"password": thepassword})

def author(request):
    return render(request, "generator/author.html")