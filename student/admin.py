from django.contrib import admin
from .models import TblStudentsAdmissions

@admin.register(TblStudentsAdmissions)
class StudentAdmin(admin.ModelAdmin):
    fields = (
       'first_name', 'last_name','other_names','gender','nationality','id_passport','date_of_birth','marital_status',
       'diocese','religion','congregation','permanent_adress','email','telephone','next_of_kin','next_of_kin_address',
       'registration_status','school','school_of_philosophy','school_of_theology','school_of_counselling',
       'anticipated_program_duration','ever_studied_at_ciu','previous_stud_id','previous_ciu_school','previous_from_year',
        'prev_to_year','colleges_attended','high_school_attended','sponsorship_community','how_you_knew_consolata',
        'disability','disability_nature','confirm_information','non_refundable_fee','copy_of_id',
        'passport_photo','coppy_of_all_degrees','copies_of_diplomas','coppy_of_qualifications','coppy_of_transcripts',
        'registration_number','image','contact','occupation','address','admission_year','month',    
    )

    list_display = (
       'first_name','last_name','nationality','id_passport','contact','email',
    )

   