from django.shortcuts import render, redirect
from django.contrib import messages
from todo_list_app.models import Todo
from todo_list_app.forms import TodoForm
from django.views.decorators.http import require_POST # this import will help to get a blank page if anybody manually type this url
                                                      # without throwing error and exception

# Create your views here.

def index(request):
    form = TodoForm()
    task_list = Todo.objects.order_by('id')
    my_dict = {'task_list':task_list, 'form':form}
    return render(request,'todo_list_app/index.html', context=my_dict)

@require_POST
def AddTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        # print(request.POST['text']) # here text is form field name
        if form.is_valid():
            # test = request.POST['test']
            # print(test)
            new_todo = Todo(text=request.POST['text']) #here Todo is the model name and here creating the model's object with
                                                       # html field value and then save it to database
            new_todo.save()
        messages.add_message(request, messages.SUCCESS, 'New Task has been added successfully.')
        return redirect('index')

def CompleteTodo(request, todo_id):
    complete_todo = Todo.objects.get(pk=todo_id)
    complete_todo.complete = True
    complete_todo.save()
    return redirect('index')

def DeleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    messages.add_message(request, messages.WARNING, 'Completed Task has been deleted.')
    return redirect('index')

def DeleteAll(request):
    task_list = Todo.objects.all()
    task_list.delete()
    messages.add_message(request, messages.WARNING, 'All Tasks have been deleted.')
    return redirect('index')

def UndoTask(request, todo_id):
    undo_task = Todo.objects.get(pk=todo_id)
    undo_task.complete = False
    undo_task.save()
    return redirect('index')

def EditTask(request, todo_id):
    if request.method == 'POST':
        updated_todo = Todo.objects.get(pk=todo_id)
        updated_todo.text = request.POST['test']
        # updated_todo.complete = True
        updated_todo.save()
        messages.add_message(request, messages.SUCCESS, 'Todo list has been updated.')
        return redirect('index')
    else:
        task = Todo.objects.get(pk=todo_id)
        # print(task)
        my_dict = {'task':task}
        return render(request, 'todo_list_app/edit_task.html', context=my_dict)
