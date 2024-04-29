from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, AuthorForm


# Create your views here.
# Using functions

# To create the datas
# def createBook(request):
#     books = Book.objects.all()
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         price = request.POST.get('price')
#
#         book = Book(title=title, price=price)
#         book.save()
#
#     return render(request, 'book.html', {'books': books})


# To see the datas in another page
def listBook(request):
    books = Book.objects.all()

    # Paginator working

    paginator = Paginator(books, 4)
    pageNumber = request.GET.get('page')

    try:
        page = paginator.get_page(pageNumber)
    except EmptyPage:
        page = paginator.page(pageNumber.numPage)

    return render(request, 'admin/listbook.html', {'books': books, 'page': page})


# To see a particular data in another page

def detailView(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'admin/detailview.html', {'book': book})


# To delete a data

def deleteView(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('/')
    return render(request, 'admin/delete.html', {'book': book})


# To update a data

def updateBook(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = BookForm(instance=book)

    return render(request, 'admin/update.html', {'form': form})


def CreateBook(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'admin/book.html', {'form': form, 'books': books})


def CreateAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()
    return render(request, 'admin/author.html', {'form': form})


def index(request):
    return render(request, 'admin/base.html')


def SearchBook(request):
    query = None
    books = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    else:
        books = []

    context = {'books': books, 'query': query}
    return render(request, 'admin/search.html', context)
