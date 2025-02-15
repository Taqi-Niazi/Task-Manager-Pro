from django.urls import path
from .views import SignupView, task_list, add_task, edit_task, delete_task , home_view
from django.contrib.auth.views import LogoutView , LoginView

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name="tasks/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
]
