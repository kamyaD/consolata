from django.urls import path
from . import views, transcipt_views

app_name = 'staff_teachers'

urlpatterns = [
    path('teachers-pay/', views.view_teachers_pay, name='teachers-pay'),
    path('admin-office/', views.admin_office, name='admin-office'),
    path('timetable/', views.create_timetable, name='timetable'),
    path('edit-table/<int:id>', views.edit_time_table, name='edit-table'),
    path('delete-table/<int:id>', views.delete_timetable_raw, name='delete-table'),
    path('fetch-sign/', views.fetch_student_class_sign, name='fetch-sign'),
    path('upload-csv/', views.upload_results_csv, name='upload-csv'),
    path('results/', views.show_exam_results, name='results'),
    path('timetable-pdf/', views.generate_timetable_pdf, name='timetable-pdf'),
    path('individual-results/<int:reg_no>', views.fetch_individual_results, name='individual-results'),
    path('upload-course-list/', views.upload_course_lists, name='upload-course-list'), 
    path('course-list/', views.show_course_list, name='course-list'),
    path('claim-form/', views.generate_claim_form, name='claim-form'),
    path('create-claim/', views.create_claim, name='create-claim'),
    path('staff-claim-form/', views.create_staff_claim_form, name='staff-claim-form'),
    path('staff-claim-form/<int:pk>/', views.view_claim_staff_form, name='staff-claim-form'),
    path('claim-form-detail/', views.view_individual_claims, name='claim-form-detail'),
    path('registrar-approve/', views.claim_form_approval_view, name='registrar-approve'),
    path('all-claims/', views.view_all_claims, name='all-claims'),
    path('edit-claim-form/<int:id>/', views.view_all_claims, name='edit-claim-form'),
    path('approve-claim/<int:id>', views.claim_form_approval_view, name='approve-claim'),
    # path('timetable/pdf/', views.timetable_pdf_view, name='timetable-pdf'),

    path('students/', transcipt_views.StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', transcipt_views.StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:reg_no>/transcript/', views.student_transcript_view, name='student-transcript'),

    path('courses/', transcipt_views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', transcipt_views.CourseDetailView.as_view(), name='course-detail'),

    path('academic-periods/', transcipt_views.AcademicPeriodListView.as_view(), name='academic-period-list'),

    path('transcripts/', transcipt_views.TranscriptEntryListView.as_view(), name='transcriptentry-list'),
    path('transcripts/add/', transcipt_views.TranscriptEntryCreateView.as_view(), name='transcriptentry-add'),

    path('summary/<int:pk>/', transcipt_views.TranscriptSummaryView.as_view(), name='transcript-summary'),

    path('courses/add/', transcipt_views.CourseCreateView.as_view(), name='course-add'),
    path('academic-periods/add/', transcipt_views.AcademicPeriodCreateView.as_view(), name='academic-period-add'),

    # path('transcripts/', transcipt_views.TranscriptSummaryListView.as_view(), name='transcript-list'),
    # path('transcripts/add/', transcipt_views.TranscriptSummaryCreateView.as_view(), name='transcript-add'),
    # path('transcripts/<int:pk>/edit/', transcipt_views.TranscriptSummaryUpdateView.as_view(), name='transcript-edit'),
    # path('transcripts/<int:pk>/', transcipt_views.TranscriptSummaryDetailView.as_view(), name='transcript-summary'),
    # path('transcripts/<int:pk>/delete/', transcipt_views.TranscriptSummaryDeleteView.as_view(), name='transcript-delete'),

    # GradeScale
    path('gradescales/', transcipt_views.GradeScaleListView.as_view(), name='gradescale-list'),
    path('gradescales/add/', transcipt_views.GradeScaleCreateView.as_view(), name='gradescale-add'),
    path('gradescales/<int:pk>/edit/', transcipt_views.GradeScaleUpdateView.as_view(), name='gradescale-edit'),
    path('gradescales/<int:pk>/', transcipt_views.GradeScaleDetailView.as_view(), name='gradescale-detail'),
    path('gradescales/<int:pk>/delete/', transcipt_views.GradeScaleDeleteView.as_view(), name='gradescale-delete'),
    # path('student-trancript/', views.student_transcript_view, name='student-trancript')


]
