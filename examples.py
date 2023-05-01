from django.db.models import Q
from django.db import models

# класс в models.py это таблицы
class students(models.Model): # определение таблицы
    firstname = models.CharField(max_length=100) # максемальная длина 100 символов
    surname = models.CharField(max_length=100)   # максемальная длина 100 символов
    age = models.IntegerField()                  # число типа int
    classroom = models.IntegerField()            # число типа int
    teacher = models.CharField(max_length=100)   # максемальная длина 100 символов

    def __str__(self):
        return self.firstname # print(students) = students.firstname

# запросы к таблице students
students.objects.all() # = SELECT * FROM student_student

################ DELETE
students.objects.all().delete()  # удалить всё записи из student_student

############### CREATE
students.objects.create(firstname = "John", surname = "Sanchez", classroom = 10) # = INSERT INTO student_student (firstname,surname,classroom) values ("John","Sanchez",10)

############## UPDATE
x = students.objects.get(classroom = 3) # ишем что изменить
x.firstname = 'Ivan' # изменяем
x.save() # сохраняем

students.objects.filter(classroom = 3) # SELECT * FROM student_student WHERE classroom = 3 

students.objects.filter(classroom = 3) & students.objects.filter(firstname = "Azamat")
students.objects.filter(classroom = 3, firstname = "Azamat")
students.objects.filter(Q(classroom = 3) & Q(firstname = "Azamat") ) # эти все записи в SQL = SELECT * FROM student_student WHERE classroom = 3 AND firstname = "Azamat"

students.objects.filter(id = 3 ,foo = 10) # & = AND
Q(id = 3) | Q(id = 4) # | = OR

Q(firstname__startswith = "R") # firstname LIKE 'R%' (с учётом регистра)
Q(firstname__istartswith = "R") # UPPER(firstname) LIKE 'R%' (без учётом регистра)

Q(firstname__endswith = "k") # firstname LIKE '%k' (с учётом регистра)
Q(firstname__iendswith = "k") # UPPER(firstname) LIKE '%K' (без учётом регистра)

Q(string__contains = "ic") # firstname LIKE '%ic%' (с учётом регистра)
Q(string__шcontains = "ic") # UPPER(firstname) LIKE '%IC%' (без учётом регистра)

Q(id__lte=10) # id <= 10    LTE = low than equal
Q(id__gte=10) # id >= 10    GTE = great than equal
Q(id__lt=10) # id < 10      LT = low than
Q(id__gt=10) # id > 10      GT = great than

Q(id__in=[0,1]) # SELECT * FROM student_student WHERE id IN (6, 3)
Q(id__isnull = True)  # SELECT * FROM student_student WHERE id IS NULL
Q(id__isnull = False)  # SELECT * FROM student_student WHERE id IS NOT NULL

students.objects.exclude(id__lt = 3)
students.objects.filter(~Q(id__lt=3)) # SELECT * FROM student_student WHERE NOT id < 3 {"id":1212}

students.objects.raw("SELECT * FROM student_student")


def dictfetchall(cursor): # из 
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

from django.db import connection

sql = "SELECT * FROM student_student"
cursor = connection.cursor()
cursor.execute(sql) 

r = cursor.fetchall() # !!!! Это Кортеж в Листе [('red',10,'yellow',255)] НЕ QuerySet (т.е dictionary = {"key":"foo"})

def dictfetchall(cursor): # из 
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

respone = dictfetchall(cursor) # Мы из Кортеж делаем dictionary =  {"key":"foo"}

######### AGGREGATIONS

from django.db.models import Max, Min, Avg, Sum

# Max 
students.objects.count() # посчитать колво записей
students.objects.all().aggregate(Sum("classroom")) # Сумма всех классов
students.objects.all().aggregate(Max("classroom")) # Максимальное знакение
students.objects.all().aggregate(Max("classroom")) # Минимальное знакение
students.objects.all().aggregate(Avg("classroom")) # Среднее знакение