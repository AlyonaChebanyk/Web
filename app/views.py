from django.shortcuts import render, redirect
import requests
import json
import datetime
from app.models import Article, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import UserForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def add_content(request):
    url = ('https://newsapi.org/v2/everything?'
           'q=technology&'
           'sortBy=popularity&'
           'apiKey=3e4a357f0451440294a28c0afbe8287f')

    response = requests.get(url)
    response = json.loads(response.text)
    articles = response['articles']

    for article in articles:
        q = 'technology'
        author = article['author']
        title = article['title']
        description = article['description']
        url_to_image = article['urlToImage']
        published_at = datetime.datetime.strptime((article['publishedAt']), "%Y-%m-%dT%H:%M:%SZ")
        content = article['content']
        Article.objects.create(q=q, author=author, title=title, description=description,
                               url_to_image=url_to_image, published_at=published_at, content=content)

    return render(request, 'show_content.html', {'articles': articles})


def show_content(request, q):
    articles = Article.objects.all().filter(q=q)
    return render(request, 'show_content.html', {'articles': articles})


def show_article(request, article_id):
    article = Article.objects.get(id=article_id)
    form = CommentForm
    comments = Comment.objects.filter(article_id=article_id)
    return render(request, 'show_article.html', {'article': article, 'form': form, 'comments': comments})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username, password)
            return HttpResponseRedirect('/nanotechnology/')

    else:
        form = UserForm()

    return render(request, 'create_user.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/nanotechnology')
            else:
                form = UserForm()
                return render(request, 'login.html', {'form': form, 'error': 'No such user'})

    elif request.method == 'GET':
        form = UserForm()
        return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def add_comment(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            print(text)
            user = User.objects.get(id=request.user.id)
            article = Article.objects.get(id=article_id)
            Comment.objects.create(text=text, user=user, article=article)
            return redirect('/{}/'.format(article_id))


def logout_user(request):
    logout(request)
    return HttpResponse('logout')
