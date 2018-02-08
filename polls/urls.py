from django.urls import path

from polls import views

urlpatterns = [
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('<str:group_name>/', views.students, name='students'),
]