from django.shortcuts import render
from django.http import HttpResponse
import random
import pyperclip

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('uppercase'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list(' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'))

    length = int(request.GET.get('length', 12))
    psw = ''
    for i in range(length):
        psw += random.choice(characters)
    pyperclip.copy(psw)
    return render(request, 'generator/password.html', {'password': psw})

def about(request):
    return render(request, 'generator/about-us.html')