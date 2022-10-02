from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('tasks/', views.tasks, name="tasks"),
    path('create-task/', views.create_new_task, name="create-task"),
    path('create-project/', views.create_new_project, name="create-project"),
    path('project-detail/<int:id>', views.project_detail, name="project-detail")
]
