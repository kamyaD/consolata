from django import forms
from student.models import TblStudentsAdmissions, StudentApplication

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = TblStudentsAdmissions
        fields = [
            # 'student',  # This is the ForeignKey to CustomUser
            'studentid','first_name','last_name','gender','image', 'nationality','date_of_birth','id_passport','contact','email','occupation','address','admission_year','month','billing_self','organization','responsible',
        'telephone','language_spoken','language_to_learn','course_type','duration','start_date','other_courses','registration_number','modality','mail_status', 'marital_status','registration_status', 'school', 'school_of_philosophy','school_of_theology','school_of_counselling', 'anticipated_program_duration', 'ever_studied_at_ciu', 'recomendation_type','disability'
        ]



class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = TblStudentsAdmissions
        fields = [
            "first_name", "last_name","sir_name", "other_names", "gender", "nationality", "id_passport", 
            "date_of_birth", "birth_place","marital_status", "diocese", "religion", "congregation", 
            "permanent_adress", "email", "telephone", "next_of_kin", "next_of_kin_address", 
            "next_of_kin_email", "next_of_kin_phone", "registration_status", "school", 
            "school_of_philosophy", "school_of_theology", "school_of_counselling", 
            "anticipated_program_duration", "ever_studied_at_ciu", "previous_stud_id", 
            "previous_ciu_school", "previous_from_year", "prev_to_year", "colleges_attended",
            "high_school_attended", "sponsorship_community", "how_you_knew_consolata",
            "disability", "disability_nature", "confirm_information",
            "non_refundable_fee", "copy_of_id", "passport_photo",
            "coppy_of_all_degrees", "copies_of_diplomas", "coppy_of_qualifications",
            "coppy_of_transcripts", "registration_number"
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "marital_status": forms.Select(attrs={"class": "form-control"}),
            "registration_status": forms.Select(attrs={"class": "form-control"}),
            "school": forms.Select(attrs={"class": "form-control"}),
            "ever_studied_at_ciu": forms.Select(attrs={"class": "form-control"}),
        }



class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        exclude = ['applicant_user', 'created_at', 'updated_at']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'permanent_address': forms.Textarea(attrs={'rows': 2}),
            'recommendation_address': forms.Textarea(attrs={'rows': 2}),
            'sponsor_address': forms.Textarea(attrs={'rows': 2}),
            'nature_of_disability': forms.Textarea(attrs={'rows': 2}),
            'next_of_kin_address': forms.Textarea(attrs={'rows': 2}),
        }
