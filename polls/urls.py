from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('<str:group_name>/', views.students, name='students'),
    path('students/add_student/', views.add_student, name='add_student'),
]