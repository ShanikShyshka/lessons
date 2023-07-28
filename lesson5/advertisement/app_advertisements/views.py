from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', name='main')

def top_sellers(request):
    return render(request, 'top-sellers.html', name='top-sallers' )