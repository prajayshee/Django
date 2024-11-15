from django.urls import path
from app import views

urlpatterns = [
    # Login page is the root URL
    path('', views.login_view, name='login'),
    
    # Task-related URLs
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('login/', views.login_view, name='login'), 
    path('signup/', views.signup_view, name='signup'), 
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.task_list, name='task_list'),  # Ensure this exists
]
