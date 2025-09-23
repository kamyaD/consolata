from django import forms
from student.models import TblStudentsAdmissions

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = TblStudentsAdmissions
        fields = [
            # 'student',  # This is the ForeignKey to CustomUser
            'studentid','first_name','last_name','image', 'nationality','date_of_birth','id_passport','contact','email','occupation','address','admission_year','month','billing_self','organization','responsible',
        'telephone','language_spoken','course_type','duration','start_date','other_courses','registration_number','modality','mail_status'
        ]
