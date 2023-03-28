from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import Create_new_task, Create_new_project
from django.contrib.auth import authenticate, login

#para saber si es superuser
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def index(request):
    title = 'Wellcome to Django course'
    return render(request, "index.html", {
        'title': title
    })

def about(request):
    username = 'adan'
    return render(request, "about.html",{
        'username': username
    })



def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello word %s </h2>" % username)


def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    #return JsonResponse(projects, safe=False) 
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def error(request):
    return render(request,'403.html')

def tasks(request):
    #tasks = get_object_or_404(Task , id=id)
    #return HttpResponse('tasks: %s ' % tasks.title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
#@user_passes_test(lambda u: not u.is_superuser)/////el codigo para que si no eres superuser no puedas acceder a esta fucionalidad
@user_passes_test(lambda u: u.is_superuser, login_url='/403/')
def create_task(request):
    if request.method == 'GET':
        #show intergaces
        return render(request, 'tasks/create_task.html',{
            'form': Create_new_task()
        })
    else:
        Task.objects.create(title = request.POST['title'],description = request.POST['description'], project_id = 1)
        return redirect("tasks")

    
@user_passes_test(lambda u: u.is_superuser, login_url='/403/')        
def create_project(request):
    if request.method == 'GET':
        return render (request, 'projects/create_project.html',{
            'form': Create_new_project()
        })
    else:
        project = Project.objects.create(name = request.POST['name'])
        return redirect("projects")


def project_detail(request, id):
    project = get_object_or_404(Project, id = id)
    tasks = Task.objects.filter(project_id = id)
    return render(request, 'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })

def imagenes(request):
    return render(request,'imagenes/cargar_imagenes.html')

def signin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                return render(request,'login.html',{
                    'error': 'El nombre de usuario o contraseña son incorrectos'
                })
            else:
                login(request,user)
                return redirect("index")
        except:
            return redirect("signin")
     