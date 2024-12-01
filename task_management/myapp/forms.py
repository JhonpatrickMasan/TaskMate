# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
        required=False
    )
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Math, Science'}),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date', 'tags']  # Include new fields

