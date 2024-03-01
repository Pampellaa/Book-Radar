import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from BookRadar.forms import LoginForm, RegisterForm
from BookRadar.models import Book, Review
from BookRadar.forms import OpinionAddForm


class IndexView(View):
    def get(self, request):
        carousel_books = list(Book.objects.all())
        random.shuffle(carousel_books)
        carousel_books = carousel_books[:3]

        books  = Book.objects.all()
        best_books = books.order_by('-ranking')[:10]

        reviews = Review.objects.all().order_by('-created')[:3]

        ctx = {'carousel_books':carousel_books, 'best_books':best_books, 'reviews':reviews}
        return render(request, 'index.html', ctx)

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        form.add_error('username', 'Invalid login details. Try again.')
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('login')
        return render(request, 'register.html', {'form': form})

class AddOpinionView(View):
    def get(self, request):
        if  request.GET.get('author_id'):
            author_id = request.GET.get('author_id')
            books = Book.objects.filter(author=author_id).values('id', 'title')
            return JsonResponse(list(books), safe=False)
        else:
            form = OpinionAddForm()
            return render(request, 'add_review.html', {'form': form})

    # def post(self, request):
    #     user = request
    #     form = OpinionAddForm(request.POST)
    #     if form.is_valid():


#  def get_books(request):
    #  author_id = request.GET.get('author_id')
    #  books = Book.objects.filter(author=author_id).values('id', 'title')
    #  return JsonResponse(list(books), safe=False)




