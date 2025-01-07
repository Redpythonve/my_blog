from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Publication, Article # type: ignore


def create(request):
    
    art1 = Article(headline='Django lets you build web apps easily')
    art1.save()
    art2 = Article(headline='Django lets bla bla bla')
    art2.save()
    art3 = Article(headline='Django lets you ble ble ble')
    art3.save()
    
    publ_1 = Publication(title='Django bli bli bli')
    publ_1.save()
    
    publ_2 = Publication(title='Django blo blo blo')
    publ_2.save()
    
    publ_3 = Publication(title='Django blu blu blu')
    publ_3.save()
    
    publ_4 = Publication(title='Django clap clap clap')
    publ_4.save()
    
    publ_5 = Publication(title='Django clep clep clep')
    publ_5.save()
    
    publ_6 = Publication(title='Django clop clop clop')
    publ_6.save()
    
    art1.publications.add(publ_1, publ_2, publ_3)
    art2.publications.add(publ_4, publ_5, publ_6)
    art3.publications.add(publ_1, publ_2, publ_3, publ_4, publ_5, publ_6)
    
    publ_1.article_set.add(art1, art3)
    publ_2.article_set.add(art1, art3)
    publ_3.article_set.add(art1, art3)
    publ_4.article_set.add(art2, art3)
    
    #result = art1.publications.all()
    #result = art2.publications.all()
    #result = art3.publications.all()
    result = publ_1.article_set.all()
    return HttpResponse(result)


