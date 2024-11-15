from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import TaskForm, SignupForm
from .models import Task
import threading
import time
from django.utils import timezone
from django.core.mail import send_mail

# Task-related views
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

# Reminder Email Function
def send_task_reminders():
    while True:
        # Wait for an hour before checking again
        time.sleep(3600)

        # Fetch tasks that need reminders
        tasks = Task.objects.filter(reminder_time__lte=timezone.now(), reminder_time__isnull=False)
        for task in tasks:
            send_mail(
                'Reminder: Task Due Soon',
                f'Your task "{task.title}" is due soon.',
                'prajaysheechauhan.com',  # Replace with your sender email
                ['prajayshee.chauhan@mitwpu.edu.in'],  # Replace with the recipient's email
                fail_silently=False,
            )
            # Clear the reminder time to avoid resending
            task.reminder_time = None
            task.save()

# Start the thread for task reminder emails
reminder_thread = threading.Thread(target=send_task_reminders)
reminder_thread.daemon = True
reminder_thread.start()

# User Authentication Views (Login, Signup, Logout)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate and login the user
            user = form.get_user()
            login(request, user)
            return redirect('task_list')  # Redirect to the task list page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in after signup
            return redirect('task_list')  # Redirect to task list after signup
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
