from django.urls import path
from todo_list_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.AddTodo, name='add'),
    path('complete/<todo_id>', views.CompleteTodo, name='complete'),
    path('deletecomplete', views.DeleteCompleted, name='deletecomplete'),
    path('deleteall', views.DeleteAll, name='deleteall'),
    path('undotask/<todo_id>', views.UndoTask, name='undotask'),
    path('edittask/<todo_id>', views.EditTask, name='edittask'),
]
