from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task


# Landing page view
def landing_page(request):
    return render(request, 'landing_page.html')

# User registration view
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate password match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')

        # Check for existing username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'register.html')

        # Check for existing email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return render(request, 'register.html')

        # Create user and log them in
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)
        return redirect('home')  # Redirect to home page

    return render(request, 'register.html')

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user and redirect to home
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again.")
            return render(request, 'login.html')

    return render(request, 'login.html')

# Authenticated home page view
@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})


# List tasks for each Kanban column
def kanban_board(request):
    tasks = {
        'TODO': Task.objects.filter(status='TODO'),
        'IN_PROGRESS': Task.objects.filter(status='IN_PROGRESS'),
        'DONE': Task.objects.filter(status='DONE'),
    }
    return render(request, 'kanban_board.html', {'tasks': tasks})

# Create a new task
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kanban_board')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

# Edit an existing task
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('kanban_board')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

# Delete a task
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('kanban_board')

@csrf_exempt
def update_task_status(request, task_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            task = Task.objects.get(pk=task_id)
            task.status = data.get('status')
            task.save()
            return JsonResponse({'success': True, 'message': 'Task updated successfully'})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Task not found'}, status=404)
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)