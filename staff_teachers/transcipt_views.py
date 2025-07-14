from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import  AcademicPeriod, Course, TranscriptEntry, TranscriptSummary
from .forms import TranscriptEntryForm  # Optional: custom form
from student.models import TblStudentsAdmissions
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import TranscriptSummary, GradeScale
from .forms import TranscriptSummaryForm, GradeScaleForm  


class StudentListView(ListView):
    model = TblStudentsAdmissions
    template_name = 'staff/student_list.html'

class StudentDetailView(DetailView):
    model = TblStudentsAdmissions
    template_name = 'staff/student_detail.html'


class CourseListView(ListView):
    model = Course
    template_name = 'staff/course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'staff/course_detail.html'


class AcademicPeriodListView(ListView):
    model = AcademicPeriod
    template_name = 'staff/academic_period_list.html'

class TranscriptEntryListView(ListView):
    model = TranscriptEntry
    template_name = 'staff/transcriptentry_list.html'

class TranscriptEntryCreateView(CreateView):
    model = TranscriptEntry
    form_class = TranscriptEntryForm  # or use fields = '__all__'
    template_name = 'staff/transcriptentry_form.html'
    success_url = reverse_lazy('staff_teachers:transcriptentry-list')

class TranscriptSummaryView(DetailView):
    model = TranscriptSummary
    template_name = 'staff/transcript_summary.html'

class CourseCreateView(CreateView):
    model = Course
    fields = ['code', 'title', 'credit', 'year', 'semester', 'school',]
    template_name = 'staff/course_form.html'
    success_url = reverse_lazy('staff_teachers:course-list')

class AcademicPeriodCreateView(CreateView):
    model = AcademicPeriod
    fields = ['academic_year', 'semester']
    template_name = 'staff/academic_period_form.html'
    success_url = reverse_lazy('staff_teachers:academic-period-list')



def student_transcript_view(request, pk):
    student = get_object_or_404(TblStudentsAdmissions, pk=pk)
    transcript_entries = TranscriptEntry.objects.filter(student=student).select_related('course', 'period').order_by('period__academic_year', 'period__semester')
    summary = TranscriptSummary.objects.filter(student=student).first()

    return render(request, 'staff/student_transcript.html', {
        'student': student,
        'entries': transcript_entries,
        'summary': summary
    })

# optional: you can use ModelForm or let Django auto-generate forms

# -------------------------
# TranscriptSummary Views
# -------------------------

# class TranscriptSummaryListView(ListView):
#     model = TranscriptSummary
#     template_name = 'staff/transcripts/transcript_list.html'
#     context_object_name = 'transcripts'


# class TranscriptSummaryCreateView(CreateView):
#     model = TranscriptSummary
#     form_class = TranscriptSummaryForm
#     template_name = 'staff/transcripts/transcript_form.html'
#     success_url = reverse_lazy('staff_teachers:transcript-list')


# class TranscriptSummaryUpdateView(UpdateView):
#     model = TranscriptSummary
#     form_class = TranscriptSummaryForm
#     template_name = 'staff/transcripts/transcript_form.html'
#     success_url = reverse_lazy('staff_teachers:transcript-list')


# class TranscriptSummaryDetailView(DetailView):
#     model = TranscriptSummary
#     template_name = 'staff/transcripts/transcript_detail.html'
#     context_object_name = 'transcript'


# class TranscriptSummaryDeleteView(DeleteView):
#     model = TranscriptSummary
#     template_name = 'staff/transcripts/transcript_confirm_delete.html'
#     success_url = reverse_lazy('staff_teachers:transcript-list')

# -------------------------
# GradeScale Views
# -------------------------

class GradeScaleListView(ListView):
    model = GradeScale
    template_name = 'staff/gradescale/gradescale_list.html'
    context_object_name = 'grades'


class GradeScaleCreateView(CreateView):
    model = GradeScale
    form_class = GradeScaleForm
    template_name = 'staff/gradescale/gradescale_form.html'
    success_url = reverse_lazy('staff_teachers:gradescale-list')


class GradeScaleUpdateView(UpdateView):
    model = GradeScale
    form_class = GradeScaleForm
    template_name = 'staff/gradescale/gradescale_form.html'
    success_url = reverse_lazy('staff_teachers:gradescale-list')


class GradeScaleDetailView(DetailView):
    model = GradeScale
    template_name = 'staff/gradescale/gradescale_detail.html'
    context_object_name = 'grade'


class GradeScaleDeleteView(DeleteView):
    model = GradeScale
    template_name = 'staff/gradescale/gradescale_confirm_delete.html'
    success_url = reverse_lazy('staff_teachers:gradescale-list')

