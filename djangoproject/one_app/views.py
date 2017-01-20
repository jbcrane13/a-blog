from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    return render(request, 'one_app/index.html', {'date' : date, 'time' : time})