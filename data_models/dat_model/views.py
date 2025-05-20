from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book


# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request,
                  'dat_model/index.html',
                  {'books': books},
                  )


def detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=book_id)
    # except:
    #     raise Http404
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        'dat_model/book_detail.html',
        {
            'title': book.title,
            'author': book.author,
            'rating': book.rating,
            'is_bestseller': book.is_bestselling,
        }
    )
