from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoItem


# Create your views here.
def todoView(request):
    all_todo_items = ToDoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})


def addtoDo(request):
    # create todo item
    # save
    # redirect the browser to /todo/
    c = request.POST['content']
    new_item = ToDoItem(content = c)
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deletetoDo(request, todo_id):
    item_to_delete = ToDoItem.objects.get(id= todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')