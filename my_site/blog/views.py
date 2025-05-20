from django.shortcuts import render
from django.http import HttpResponse

from datetime import date

posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Dima',
        'date': date(2022, 9, 12),
        'tittle': 'Mountain Hiking',
        'excerpt': "There's nothing like the views you get when hiking in the mountains.",
        'content': '''
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam labore laudantium quidem quisquam
            sapiente?
            A adipisci amet assumenda aut eveniet iste iure nemo numquam quo temporibus velit veniam, vero
            voluptatibus?
        '''
    }
]


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/all-posts.html')


def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
