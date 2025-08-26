from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('online-application/', views.online_application, name='online-application'),
    path('submit-online-app/', views.submit_online_application,name='submit-online-app'),
    path('timetable/', views.fetch_timetable, name='timetable'),
    path('get-student-record/', views.view_individual_sudent, name='get-student-record'),
    path('student-results/', views.fetch_student_results, name='student-results'),
]

