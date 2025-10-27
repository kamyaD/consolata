from django.urls import path
from . import views

app_name = 'staff_teachers'

urlpatterns = [
    path('teachers-pay/', views.view_teachers_pay, name='teachers-pay'),
    path('admin-office/', views.admin_office, name='admin-office'),
    path('timetable/', views.create_timetable, name='timetable'),
    path('edit-table/<int:id>', views.edit_time_table, name='edit-table'),
    path('delete-table/<int:id>', views.delete_timetable_raw, name='delete-table'),
    path('fetch-sign/', views.fetch_student_class_sign, name='fetch-sign'),

    path('timetable-pdf/', views.generate_timetable_pdf, name='timetable-pdf'),
    path('claim-form/', views.generate_claim_form, name='claim-form'),
    path('create-claim/', views.create_claim, name='create-claim'),
    path('staff-claim-form/', views.create_staff_claim_form, name='staff-claim-form'),
    path('staff-claim-form/<int:pk>/', views.view_claim_staff_form, name='staff-claim-form'),
    path('claim-form-detail/', views.view_individual_claims, name='claim-form-detail'),
    path('registrar-approve/', views.claim_form_approval_view, name='registrar-approve'),
    path('all-claims/', views.view_all_claims, name='all-claims'),
    path('edit-claim-form/<int:id>/', views.view_all_claims, name='edit-claim-form'),
    path('approve-claim/<int:id>', views.claim_form_approval_view, name='approve-claim'),
    path('student-result-upload/', views.upload_results_csv, name='student-result-upload'),
    path('course-list/', views.upload_course_list, name='course-list'),
    path('view-course-list/', views.view_all_courses, name='view-course-list'),
    path('edit-course/<int:id>/', views.edit_course_list, name='edit-course'),
    path('create-course-list/', views.create_course_list, name='create-course-list'),
    path('view-results/', views.show_exam_results, name='view-results'),
    path('populate-transcript/<int:student_id>', views.populate_transcript, name='populate-transcript'),
    path('edit-result/<int:id>', views.edit_result, name='edit-result'),
    path('transcript/pdf/<int:student_id>/', views.generate_transcript_pdf, name='generate_transcript_pdf'),
    path('generate-transcript-pdf/<int:student_id>', views.generate_transcript_pdf, name='generate-transcript-pdf'),
    path('language-portal/', views.language_portal, name="language-portal"),
    path('clc-claim-form', views.clc_claim_form, name='clc-claim-form'),
    path('psychology/', views.psychology_list, name='psychology_list'),
    path('psychology/register/', views.psychology_register, name='psychology_register'),
]
