from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.

def index(request):
    context = {
    # "time":now,
    "hurro": datetime.datetime.now
    }
    print datetime.datetime.now
    return render(request, "timedisplay/index.html", context)
def show(request):
    print(request.method)
    return render(request, "timedisplay/show_users.html")
