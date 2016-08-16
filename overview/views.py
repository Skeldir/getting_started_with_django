from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def overview(request):
  response = request.META
  return HttpResponse(response.__str__())

def session(request):
  if request.session.get("hello", default=False):
    return HttpResponse("Hello "+request.session["hello"])

  request.session["hello"] = "Cookie-World"
  request.session.expire(15)
  return HttpResponse("No cookie set yet...")
