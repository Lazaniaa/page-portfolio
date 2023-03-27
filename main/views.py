from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')
def indexx(request):
    return render(request, 'main/about.html')
def indexxx(request):
    return render(request, 'main/t-join.html')
def indexxxx(request):
    return render(request, 'main/vertical-weld.html')
def indexxxxx(request):
    return render(request, 'main/join.html')
