from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(
    attrs = {'class':"form-control", 'placeholder':"Enter todo e.g. Delete junk files", 'aria-label':"Todo", 'aria-describedby':"add-btn"}
    ))

class EditForm(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(
    attrs = {'class':"form-control", 'aria-label':"Todo", 'aria-describedby':"add-btn", 'value':"{{task.text}}"}
    ))
