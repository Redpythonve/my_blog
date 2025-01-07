from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post

def queries(request):
    
    
    authors = Author.objects.all()
    
    author = Author.objects.get(id=2)
    author_2 = Author.objects.get(id=28)
    
    limits = Author.objects.all()[:10]
    
    offsets = Author.objects.all()[5:10]
    
    orders = Author.objects.all().order_by('email')
    
    orders_2 = Author.objects.all().order_by('email')[:10]
    
    filters = Author.objects.filter(id__lte=10)
    
    filters_2 = Author.objects.filter(name__contains="t")
    
    
    
    
    return render (request, 'post/queries.html',
                   
        {
        'authors': authors, 
        'author': author, 
        'author_2': author_2, 
        'limits': limits,
        'offsets': offsets, 
        'orders': orders, 
        'orders_2': orders_2,
        'filters': filters,
        'filters_2': filters_2
        }
        
        )


def updates(request):
    
    author = Author.objects.get(id=2)
    author.name = 'John'
    author.email = 'john@gmail.com'
    author.save()
    return HttpResponse('Author updated successfully')

    
   

# Create your views here.
