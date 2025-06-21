from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from django.urls import reverse

from todo_app.models import Todo
from todo_app.forms import TodoForm



class TodoListView(ListView):
    model=Todo
    template_name="bootstrap/todo_list.html"
    context_object_name="todos"

# def todo_list(request):
#     todos = Todo.objects.all() # => query set 
#     return render(
#         request,
#         "bootstrap/todo_list.html",
#         {"todos": todos}
#     )

class TodoDeleteView(DeleteView):
    model=Todo

    def get_success_url(self):
        return reverse("todo-list")
    
        
    
    # def get(self, request, *args, **kwargs):
    #     # Call delete on GET request directly (not recommended for production)
    #     return self.post(request, *args, **kwargs)

# def todo_delete(request,id):
#     todo=Todo.objects.get(id=id) #select * from todo where id=id
#     todo.delete()
#     return HttpResponseRedirect("/")







class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "bootstrap/todo_create.html"


    def get_success_url(self):
        return reverse("todo-list")

# def todo_create(request):
#     if request.method=='GET':
#         return render(request,"bootstrap/todo_create.html")
#     else:
#         Todo.objects.create(title=request.POST["title"])
#         return HttpResponseRedirect("/")



class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "bootstrap/todo_update.html"

    def get_success_url(self):
        return reverse("todo-list")
    
# def todo_update(request,id):
#     if request.method == "GET":
#         todo= Todo.objects.get(id=id)
#         return render (
#             request,
#             "bootstrap/todo_update.html",
#             {"todo":todo}

#         )
#     else:
#         todo=Todo.objects.get(id=id)
#         todo.title=request.POST["title"]
#         todo.save()
#         return HttpResponseRedirect("/")