from django.shortcuts import render

# Create your views here.

def button(req):
    return render(req, "demo.html")