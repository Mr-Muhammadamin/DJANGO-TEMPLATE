from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.
def main_view(request: HttpRequest):
    return render(request ,"core/index.html")