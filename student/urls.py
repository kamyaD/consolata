from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='student-list'),
    # path('online-application/', views.online_application, name='online-application'),
    # path('submit-online-app/', views.submit_online_application,name='submit-online-app'),
    path('timetable/', views.fetch_timetable, name='timetable'),
    path('get-student-record/', views.view_individual_sudent, name='get-student-record'),
    path('student-results/', views.fetch_student_results, name='student-results'),
    path('update-student/<int:pk>/', views.update_student, name='update-student'),
    path('apply/', views.application_form_view, name='application_form'),
    path('apply/submit/', views.application_submit_ajax, name='application_submit_ajax'),
    path('applicants/', views.applicants_list_view, name='applicants_list'),
    path('applicants/<int:application_id>/', views.applicant_detail_view, name='applicant_detail'),


]

