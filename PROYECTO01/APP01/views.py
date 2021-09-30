from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def login_success(request):
    return render(request, "APP01/show.html")

