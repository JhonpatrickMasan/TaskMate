from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Built-in login view with custom template
    path('logout/', LogoutView.as_view(next_page='landing_page'), name='logout'),  # Logout and redirect to landing
    path('home/', views.home, name='home'),  # Authenticated home page
    path('tasks', views.kanban_board, name='kanban_board'),  # Display Kanban board
    path('task/create/', views.create_task, name='create_task'),  # Create task
    path('task/edit/<int:pk>/', views.edit_task, name='edit_task'),  # Edit task
    path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),  # Delete task
    path('update-task-status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]
