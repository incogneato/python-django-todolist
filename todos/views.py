# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def show(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'show.html', context)

def create(request):
    if(request.method == 'POST'):
        title = request.POST.get('title')
        text_body  = request.POST.get('text')

        todo = Todo(title=title, text=text_body)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')

def complete_todo(request, id):
    todo = Todo.objects.get(pk=id)
    todo.complete = True
    todo.save()

    return redirect('index')

def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')
