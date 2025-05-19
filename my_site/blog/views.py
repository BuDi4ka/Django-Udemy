from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome page")


def posts(request):
    return HttpResponse("All posts")


def post(request, post_id):
    return HttpResponse(f"Post {post_id}")