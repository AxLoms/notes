from django.shortcuts import render
from tinder.models import Tinder
from tinder.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect


    
# Create your views here.

def tinder(request):
    print("Работает...")
    
    return render(request, 'tinder.html' )


def helpa(request):
    print("ОНО ЖИВОЕ!!!")    
    return render(request, 'helpaa.html')


def description(request):
    information = {'name':'Саша','age':'15 лет','gender':'МУЖЧИНА','city':'Пенза','hobbies':['computers games','Python','boxing','gym','study in the school']}
    return render(request, 'description.html',information)


def profile(request):
    print("Привет как дела?...")
    return render(request, 'profile.html')


def registration(request):
    print("Это кто такой!!!...")
    return render(request, 'registration.html')


def login_page(request):
    print("Система поиска")

    return render(request, 'auhtorization.html')


def process_registration(request):
    print(1)
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if  User.objects.filter(username = email).exists():
        return render(request, 'registration.html',{'error':"Данные почты или пароль уже заняты"})

    if len(password) < 6:
        return render(request, 'registration.html',{'error':"Слишком длинный или короткий"})
    user = User.objects.create(username=email, first_name=name)
    user.set_password(password)
    user.save()
    print(2)
    print(email,password)
    return render(request, 'registration.html')

   


def process_login(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email,password)
    user = authenticate(request, username=email, password=password)
    print(user)
    
    if user is not None:
        login(request,user)
        return redirect("/")
    
    return render(request, 'auhtorization.html', {'error':'Увы это мы не нашли:('})


def notes(request):
    print("Привет как дела?...")
    notes = Tinder.objects.all()
    
    if request.user.is_authenticated:
        notes = notes.filter(author = request.user)
    else:
        notes = notes.filter( author__isnull=True)
    information = {'notes':notes}
    return render(request, 'notes.html',information)


def form_notes(request):
    print("Ой кто-то пришёл)")
    print(request.GET)
    name = request.GET['name']
    description = request.GET['description']
    author = request.user
    print(name,description,author)
    if  not request.user.is_authenticated:
        author = None
    
    Tinder.objects.create(name=name,description=description,author = author)
    return redirect("/notes") 

def delit_notes(request,id):
    print("УДАЛЕНИЕ")
    print(id)      
    record = Tinder.objects.get(id=id)    
    record.delete()
    return redirect("/notes")


