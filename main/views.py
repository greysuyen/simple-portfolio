from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now().strftime("%B %d, %Y")
    return render(request, 'main/index.html', {
        "main" : now
    })