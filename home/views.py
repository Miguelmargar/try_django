from django.shortcuts import render
from .models import Book


# Create your views here.
def get_index(request):
    book_items = Book.objects.all()   # this gets all from database sqlite3
    return render(request, "home/index.html", {"books": book_items})