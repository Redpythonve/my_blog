from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Reporter, Article
from datetime import date


def create(request):
    
    # Crear un nuevo reportero
    rep = Reporter(first_name='John', last_name='Doe', email='crnlo@gmail.com')# type: ignore
    rep.save()
    
    art1 = Article(headline='This is a', pub_date=date(2022,5,20), reporter=rep)# type: ignore
    art2 = Article(headline='This is a bla bla bla', pub_date=date(2023,5,15), reporter=rep)# type: ignore
    art3 = Article(headline='This is a ble ble ble', pub_date=date(2024,5,10), reporter=rep)# type: ignore
    art1.save()
    art2.save()
    art3.save()
    
    # result = art1.reporter.first_name + " " + art1.reporter.last_name + " " + art1.headline + " " + str(art1.pub_date) + "<br>" + art2.reporter.first_name + " " + art2.reporter.last_name + " " + art2.headline + " " + str(art2.pub_date) + "<br>" + art3.reporter.first_name + " " + art3.reporter.last_name + " " + art3.headline + " " + str(art3.pub_date)
    result = rep.article_set.all()
    return HttpResponse(result)
# Create your views here.
