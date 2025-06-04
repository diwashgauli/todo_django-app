from django.shortcuts import render
from django.http import HttpResponseRedirect

from todo_app.models import Todo

def todo_list(request):
    todos = Todo.objects.all() # => query set 
    return render(
        request,
        "todo_list.html",
        {"todos": todos}
    )

def todo_delete(request,id):
    todo=Todo.objects.get(id=id) #select * from todo where id=id
    todo.delete()
    return HttpResponseRedirect("/")