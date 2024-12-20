from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

def queries(request):
    authors = Author.objects.all()
    return render(request, 'post/queries.html', {'authors': authors})

# Create your views here.
