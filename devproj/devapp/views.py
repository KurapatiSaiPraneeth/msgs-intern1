from django.shortcuts import render
from .models import Book,Author

# Create your views here.
def Index(request):
    return render(request,'devapp/index.html')

def author(request):
    authors=Author.objects.all()
    return render(request,'devapp/filter_by_author.html',{'authors':authors})

def Filter_by_author(request):
    name=request.GET['name']
    author=Author.objects.get(author_name=name)
    records=author.book_set.all()
    
    return render(request,'devapp/author.html',{'books':records,'name':name})

def book(request):
    books=Book.objects.all()
    return render(request,'devapp/filter_by_book.html',{'books':books})

def Filter_by_book(request):
    name=request.GET['name']
    book=Book.objects.get(book_name=name)
    records=book.author.all()
    return render(request,'devapp/book.html',{'authors':records,'name':name})    