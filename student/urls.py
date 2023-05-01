from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='student_data'),
    path('clear_student', views.clear_student, name='clear_student'),
    path('create/', views.create_student, name='create_student'),
    path('createfrom', views.create_student_form, name='create_student_form'),
    path('only/', views.only, name='only'),
]
