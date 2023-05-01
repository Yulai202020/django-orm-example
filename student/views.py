from django.shortcuts import render,redirect
from .models import Student
from django.db import connection
from django.shortcuts import redirect
from django.db.models import Q, F
from django.views.decorators.csrf import csrf_protect


# delete all students
@csrf_protect
def clear_student(request):
    Student.objects.all().delete()
    return redirect('/student')

# form for create students
@csrf_protect
def create_student_form(request):
    return render(request, 'createform.html')

# create student in the databse
@csrf_protect
def create_student(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data.get('firstname')
        surname = data.get('surname')
        age = data.get('age')
        classroom = data.get('classroom')
        teacher = data.get('teacher')
        cr = Student.objects.create(firstname = firstname, surname=surname, age = age, classroom = classroom, teacher = teacher)
        cr.save()
    return redirect('/student')

# students list
@csrf_protect
def student_list(request):

    posts = Student.objects.all()
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})

############ курс

@csrf_protect
def only_(request):

    posts = Student.objects.filter(classroom=3).only('firstname','age') # select firstname, age from student
    print(posts)
    print(connection.queries)
    return render(request, 'only.html',{'posts':posts})


@csrf_protect
def only_(request):

    posts = Student.objects.raw("SELECT * FROM student_student") # просто пишеш запрос
    print(posts)
    print(connection.queries)
    return render(request, 'only.html',{'posts':posts})

def dictfetchall(cursor): # из 
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

@csrf_protect
def only_(request):

    sql = "SELECT * FROM student_student"
    cursor = connection.cursor()
    cursor.execute(sql) # просто пишеш запрос
    
    r = cursor.fetchall() # !!!! Это Кортеж в Листе [('red',10,'yellow',255)] НЕ QuerySet (т.е dictionary = {"key":"foo"})

    respone = dictfetchall(cursor) # Мы из Кортеж делаем dictionary =  {"key":"foo"}

    print(respone)
    print(connection.queries)
    return render(request, 'only.html',{'posts':respone})

@csrf_protect
def only(request):
    posts = Student.objects.filter(Q(firstname__istartswith = "a")) # select * from student where classroom in (6,3)
    print(posts)
    print(connection.queries)
    return render(request, 'only.html',{'posts':posts})