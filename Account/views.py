from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from Bookapp.models import Book


# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matched')
            return redirect('register')
    return render(request, 'account/register.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('listbook')
        else:
            messages.info(request, 'Please enter valid details')
            return redirect('login')
    return render(request, 'account/login.html')


def ListBook(request):
    book = Book.objects.all()
    paginator = Paginator(book, 6)
    pageNumber = request.GET.get('page')

    try:
        page = paginator.get_page(pageNumber)
    except EmptyPage:
        page = paginator.page(pageNumber.numPage)

    context = {'book': book, 'page': page}
    return render(request, 'account/accountlistbook.html', context)
