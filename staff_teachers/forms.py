from django import forms
from .models import TimetableEntry, TblClaimSheet, ClaimForm
from student.models import CourseLists
from staff_teachers.models import TblTeachersPay, PsychologyRegistration

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




class CourseCSVUploadForm(forms.Form):
    file = forms.FileField()


class CourseEditForm(forms.ModelForm):
    
    class Meta:
        model = CourseLists
        fields = ['course_code', 'course_title', 'year', 'semester', 'credit']

class ClcClaimForm(forms.ModelForm):
    class Meta:
        model = TblTeachersPay
        fields = '__all__'
        



class PsychologyRegistrationForm(forms.ModelForm):
    class Meta:
        model = PsychologyRegistration
        fields = ['name', 'number', 'email', 'gender', 'category', ]
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'},choices=[
                ('Male', 'Male'),
                ('Female', 'Female'),
                ('Other', 'Other'),
            ]),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=[
            ('Personal development', 'Personal development'),
            ('Priest', 'Priest'),
            ('Brothers', 'Brothers'),
            ('Sisters', 'Sisters'),
            ('Formees', 'Formees'),
            ('Others', 'Others'),
            ]),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'registration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'payment_code': forms.TextInput(attrs={'class': 'form-control'}),
            # 'adm': forms.TextInput(attrs={'class': 'form-control'}),
        }
