from django.shortcuts import render
from .models import Author


# Create your views here.
def get_index(request):
    authors = Author.objects.all()   # this gets all from database sqlite3
    return render(request, "home/index.html", {"authors": authors})