from django.shortcuts import render, redirect
from .models import Topic, Article #imported
from .forms import InputForm
from . import forms
#from django.http import HttpResponse



#   Create your views here.

def create_article(request):
    if request.method == "POST":
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:topics')
        else:
            print("an error has occured")
    form = forms.ArticleForm()
    return render(request, 'input.html', {'form':form})


def show_articles(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles':articles})


def create_topic(request):
    if request.method == "POST":
        form = forms.TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:topics')
        else:
            print("an error has occured")
    form = forms.TopicForm()
    return render(request, 'input.html', {'form':form})

def send_input_data(request):
    form = InputForm()
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            print("form valid")
        else:
            print("form not valid")
    return render(request,'input.html',{'form':form})

def show_topics(request):
    topics = Topic.objects.all()
    return render(request, 'topics.html', {'topics':topics})

def showarticle(request):
    title="My First Article"
    article="""
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
    author = "Matshehla Konaite"
    return render(request, 'blog.html',{'title':title, 'article':article})

def show_cat(request):
    return render(request,'cat.html',{'form':''})

def show_cake(request):
    return render(request,'cake.html',)

def show_tut(request):
    return render(request,'graduations.html',)

def show_computer(request):
    return render(request,'computer.html',)

def show_underwater(request):
    return render(request,'underwater.html',)

def show_weeds(request):
    return render(request,'weeds.html',)

#testing
def index(request):
    return render(request,'index.html',)



#   Create your views here.
# def index(request):
#    return HttpResponse("AppTwo Index view")
