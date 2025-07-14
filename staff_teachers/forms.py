from django import forms
from .models import TimetableEntry, TblClaimSheet, ClaimForm, TranscriptEntry, TranscriptSummary, GradeScale

class TimetableEntryForm(forms.ModelForm):
    class Meta:
        model = TimetableEntry
        fields = [ 'day','class_level','course_code_first','course_title_first','lecturer_first',
            'first_room','course_code_second','course_title_second','lecturer_second','second_room',
            'after_break_course_code_first','after_break_course_title_first','after_break_lecturer_first',
            'after_break_first_room','after_break_course_code_second','after_break_course_title_second','after_break_lecturer_second',
            'after_break_second_room','after_lunch_course_code_first','after_lunch_course_title_first','after_lunch_lecturer_first',
            'after_lunch_first_room','after_lunch_course_code_second','after_lunch_course_title_second','after_lunch_lecturer_second',
            'after_lunch_second_room']
        
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control', 'id': 'day'}),
            'class_level': forms.Select(attrs={'class': 'form-control', 'id': 'class-level'}),
            'course_code_first': forms.TextInput(attrs={'class': 'form-control'}),
            'course_title_first': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'lecturer_first': forms.TextInput(attrs={'class': 'form-control'}),
            'first_room': forms.TextInput(attrs={'class': 'form-control'}),

            'course_code_second': forms.TextInput(attrs={'class': 'form-control'}),
            'course_title_second': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'lecturer_second': forms.TextInput(attrs={'class': 'form-control'}),
            'second_room': forms.TextInput(attrs={'class': 'form-control'}),

            'after_break_course_code_first': forms.TextInput(attrs={'class': 'form-control'}),
            'after_break_course_title_first': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'after_break_lecturer_first': forms.TextInput(attrs={'class': 'form-control'}),
            'after_break_first_room': forms.TextInput(attrs={'class': 'form-control'}),

            'after_break_course_code_second': forms.TextInput(attrs={'class': 'form-control'}),
            'after_break_course_title_second': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'after_break_lecturer_second': forms.TextInput(attrs={'class': 'form-control'}),
            'after_break_second_room': forms.TextInput(attrs={'class': 'form-control'}),

            'after_lunch_course_code_first': forms.TextInput(attrs={'class': 'form-control'}),
            'after_lunch_course_title_first': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'after_lunch_lecturer_first': forms.TextInput(attrs={'class': 'form-control'}),
            'after_lunch_first_room': forms.TextInput(attrs={'class': 'form-control'}),

            'after_lunch_course_code_second': forms.TextInput(attrs={'class': 'form-control'}),
            'after_lunch_course_title_second': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'after_lunch_lecturer_second': forms.TextInput(attrs={'class': 'form-control'}),
            'after_lunch_second_room': forms.TextInput(attrs={'class': 'form-control'}),

            'lecturer': forms.TextInput(attrs={'class': 'form-control'}),
            'time_slot': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TblClaimSheetForm(forms.ModelForm):
    class Meta:
        model = TblClaimSheet
        fields = [ 'month']


class ClaimFormForm(forms.ModelForm):
    class Meta:
        model = ClaimForm
        fields = [ 'month']


class TranscriptEntryForm(forms.ModelForm):
    class Meta:
        model = TranscriptEntry
        fields = ['student', 'course', 'period', 'score']


class TranscriptSummaryForm(forms.ModelForm):
    class Meta:
        model = TranscriptSummary
        fields = '__all__'

class GradeScaleForm(forms.ModelForm):
    class Meta:
        model = GradeScale
        fields = '__all__'