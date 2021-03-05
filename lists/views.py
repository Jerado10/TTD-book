from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    response = HttpResponse('<html><title>To-Do List</title></html>')
    return response