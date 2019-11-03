from django.shortcuts import render

from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def gig_detail(request, id):
    return render(request,'gig_detail.html',{})
