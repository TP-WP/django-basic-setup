from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = "Welcome to Django course"
    return render(request, "index.html", {
        "title": title
    })


def about(request):
    return render(request, "about.html")


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        'projects': projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        'tasks': tasks
    })


def create_new_task(request):
    if (request.method == "GET"):
        return render(request, "tasks/create_task.html", {
            'form': CreateNewTask()
        })
    elif (request.method == "POST"):
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect("tasks")


def create_new_project(request):
    if (request.method == "GET"):
        return render(request, "projects/create_project.html", {
            'form': CreateNewProject()
        })
    elif (request.method == "POST"):
        Project.objects.create(
            name=request.POST['name'])
        return redirect("projects")


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "projects/project.html", {
        "project": project,
        "tasks": tasks
    })
