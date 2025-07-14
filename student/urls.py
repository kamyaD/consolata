from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('online-application/', views.online_application, name='online-application'),
    path('submit-online-app/', views.submit_online_application,name='submit-online-app'),
    path('results/', views.student_result,name='results'),
    path('timetable/', views.fetch_timetable, name='timetable'),
    path('generate-result-pdf/', views.generate_results_pdf, name='generate-result-pdf'),
    path('get-student-record/', views.view_individual_sudent, name='get-student-record')
]

