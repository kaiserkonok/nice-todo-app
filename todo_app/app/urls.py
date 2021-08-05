from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.app, name='app'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('register/', views.register, name='register'),
    path('login/', views.user_log_in, name='login'),
    path('logout/', views.user_log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('<int:todo_id>/delete_todo/', views.delete_todo, name='delete_todo'),
]
