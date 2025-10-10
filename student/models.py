from django.db import models
from django.utils.timezone import now
from userauth.models import CustomUser
from django.conf import settings
# from staff_teachers.models import CourseResults


def get_year_choices():
    current_year = now().year
    return [(year, year) for year in range(2000, current_year + 1)]

MONTH_CHOICES = [
    ('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'),
    ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'),
    ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')
]

TYPE_OF_SPONSOR_CHOICES = [
    ('Self', 'Self'),
    ('Congregation', 'Congregation')
]

LANGUAGE_CHOICES = [
    ('English', 'English'),
    ('French', 'French'),
    ('Spanish', 'Spanish'),
    ('Arabic', 'Arabic'),
    ('Chinese', 'Chinese'),
    ('Russian', 'Russian'),
    ('German', 'German'),
    ('Portuguese', 'Portuguese'),
    ('Hindi', 'Hindi'),
    ('Japanese', 'Japanese'),
    ('Italian', 'Italian'),
    ('Kiswahili', 'Kiswahili'),
    ('Kenyan Sign Language', 'Kenyan Sign Language'),
    ('Korean', 'Korean'),
    ('Turkish', 'Turkish'),
    ('Bengali', 'Bengali'),
    ('Persian', 'Persian'),
    ('Punjabi', 'Punjabi'),
    ('Urdu', 'Urdu'),
    ('Indonesian', 'Indonesian'),
    ('Malay', 'Malay'),
    ('Tamil', 'Tamil'),
    ('Thai', 'Thai'),
    ('Dutch', 'Dutch'),
    ('Polish', 'Polish'),
    ('Romanian', 'Romanian'),
    ('Vietnamese', 'Vietnamese'),
    ('Ukrainian', 'Ukrainian'),
    ('Greek', 'Greek'),
    ('Hebrew', 'Hebrew'),
    ('Amharic', 'Amharic'),
]

TYPE_OF_COURSE_CHOICES = [
    ('Normal', 'Normal'),
    ('Special', 'Special'),
    ('Evening & Weekend', 'Evening & Weekend'),
    ('Onsite', 'Onsite')
] 

DURATION_CHOICES = [
    ('1 Months', '1 Months'),
    ('2 Months', '2 Months'),
    ('3 Months', '3 Months'),
    ('4 Months', '4 Months'),
    ('1 Year', '1 Year'),
    ('2 Year', '2 Year'),
    ('3 Year', '3 Year'),
    ('4 Year', '4 Year'),
]

MODALITY_OF_STUDY_CHOICES = [
    ('On Campus Study', 'On Campus Study'),
    ('Online Study', 'Online Study'),
    ('Both', 'Both')
]

OTHER_COURSES_CHOICES = [
    ('None', 'None'),
    ('Computer Packages', 'Computer Packages'),
    ('ICT Basic Training', 'ICT Basic Training'),
    ('English', 'English'),
    ('TOEFL', 'TOEFL'),
    ('IELTS', 'IELTS'),
    ('PITMAN', 'PITMAN'),
    ('ITALIAN', 'ITALIAN'),
    ('CIL', 'CIL'),
    ('FRENCH', 'FRENCH'),
    ('DELF', 'DELF'),
    ('DALF', 'DALF'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

MARITAL_STATUS_CHOICES = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Priest', 'Priest'),
    ('Deacon', 'Deacon'),
    ('Sister', 'Sister'),
    ('Brother', 'Brother'),
    ('Seminarian', 'Seminarian')
]

REGISTRATION_STATUS_CHOICES = [
    ('Full Time', 'Full Time'),
    ('Auditing', 'Auditing'),
    ('Weekend', 'Weekend'),
    ('Part-Time', 'Part-Time'),
    ('Evening Study', 'Evening Study'),
    ('Distance Learning', 'Distance Learning')
]

SCHOOL_CHOICES = [
    ('School Of Philosophy', 'School Of Philosophy'),
    ('School Of Theology', 'School Of Theology'),
    ('School Of Counselling Psychology', 'School Of Counselling Psychology'),

]

SCHOOL_OF_PHILOSOPHY = [
    ('Baccalaureate In Philosophy', 'Baccalaureate In Philosophy'),
    ('Bachelor Of Philosophy', 'Bachelor Of Philosophy'),
    ('Diploma In Philosophy', 'Diploma In Philosophy'),
    ('Certificate In Philosophy', 'Certificate In Philosophy'),
    ('No Award', 'No Award'),
]

SCHOOL_OF_THEOLOGY = [
    ('Baccalaureate In Theology (STB)', 'Baccalaureate In Theology (STB)'),
    ('Bachelor Of Theology (BATh)', 'Bachelor Of Theology (BATh)'),
    ('Diploma In Theology', 'Diploma In Theology'),
    ('Diploma In Religious Studies', 'Diploma In Religious Studies'),
    ('Certificate In Theology', 'Certificate In Theology'),
    ('Certificate In Religious Studies', 'Certificate In Religious Studies'),
    ('No Award', 'No Award'),
]

SCHOOL_OF_COUNSELLING_PSYCHOLOGY =[
    ('Bachelor In Counselling Psychology', 'Bachelor In Counselling Psychology'),
    ('Diploma In Counselling Psychology', 'Diploma In Counselling Psychology'),
    ('Certificate In Counselling Psychology', 'Certificate In Counselling Psychology'),
    ('No Award', 'No Award')
]

PROGRAM_DURATION = [
    ('1 Years', '1 Year'),
    ('2 Years', '2 Years'),
    ('3 Years', '3 Years'),
    ('4 Years', '4 Years')
]

YES_NO_CHOICES =[
    ('Yes','Yes'),
    ('No', 'No')
]

RECOMMENDATION_CHOICES = [
    ('Congregation', 'Congregation'),
    ('Diocese', 'Diocese'),
    ('Organisation','Organisation')
]


class TblStudentsAdmissions(models.Model):
    studentid = models.AutoField(db_column='studentID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    sir_name = models.CharField(max_length=100, null=True, blank=True)
    other_names = models.CharField(max_length=100, null=True, blank=True)
    birth_place = models.CharField(max_length=100, null=True, blank=True)
    diocese = models.CharField(max_length=100, null=True, blank=True)
    congregation = models.CharField(max_length=100, null=True, blank=True)
    permanent_adress = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_address = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_email = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,null=True, blank=True)
    image = models.FileField(upload_to='consolata_admin/student', null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    id_passport = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    admission_year = models.CharField(max_length=20, blank=True, null=True, default=now().year)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    billing_self = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    responsible = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    language_spoken = models.CharField(max_length=100, null=True, blank=True)
    language_to_learn = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    course_type = models.CharField(max_length=100, choices=TYPE_OF_COURSE_CHOICES)
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES)
    start_date = models.DateField(blank=True, null=True)
    other_courses = models.CharField(max_length=100, choices=OTHER_COURSES_CHOICES)
    sponsor = models.CharField(max_length=254, null=True, blank=True)
    registration_number = models.IntegerField(blank=True, null=True)
    modality = models.CharField(max_length=100, choices=MODALITY_OF_STUDY_CHOICES)
    mail_status = models.CharField(max_length=20, null=True, blank=True)
    type_of_sponsorship =  models.CharField(max_length=254,choices=TYPE_OF_SPONSOR_CHOICES, null=True, blank=True)
    marital_status = models.CharField(max_length=254,choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    registration_status = models.CharField(max_length=254,choices=REGISTRATION_STATUS_CHOICES, null=True, blank=True)
    school = models.CharField(max_length=254,choices=SCHOOL_CHOICES, null=True, blank=True)
    school_of_philosophy = models.CharField(max_length=254, choices=SCHOOL_OF_PHILOSOPHY, null=True, blank=True)
    school_of_theology = models.CharField(max_length=254, choices=SCHOOL_OF_THEOLOGY,null=True, blank=True)
    school_of_counselling = models.CharField(max_length=254, choices=SCHOOL_OF_COUNSELLING_PSYCHOLOGY, blank=True, null=True)
    anticipated_program_duration = models.CharField(max_length=254, choices=PROGRAM_DURATION, null=True, blank=True) 
    ever_studied_at_ciu = models.CharField(max_length=254, choices=YES_NO_CHOICES, null=True, blank=True)
    previous_stud_id = models.CharField(max_length=100, null=True, blank=True)
    previous_ciu_school = models.CharField(max_length=100, null=True, blank=True)
    previous_from_year = models.CharField(max_length=100, null=True, blank=True)
    prev_to_year = models.CharField(max_length=100, null=True, blank=True)
    colleges_attended = models.CharField(max_length=100, null=True, blank=True)
    high_school_attended = models.CharField(max_length=100, null=True, blank=True)
    sponsor_recomendation = models.CharField(max_length=100, null=True, blank=True)
    recommending_authority = models.CharField(max_length=100, null=True, blank=True)
    recommending_congregation = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    sponsor_address = models.CharField(max_length=250, null=True, blank=True)
    sponsor_phone = models.CharField(max_length=250,null=True, blank=True)
    sponsor_email = models.CharField(max_length=250,null=True, blank=True)
    recomendation_type = models.CharField(max_length=254, choices=RECOMMENDATION_CHOICES, null=True, blank=True)
    disability = models.CharField(max_length=254, choices=YES_NO_CHOICES, null=True, blank=True)
    how_fee_will_be_paid = models.CharField(max_length=250,null=True, blank=True)
    recomendation_address = models.CharField(max_length=250, null=True, blank=True)
    recomendation_email = models.CharField(max_length=250, null=True, blank=True)
    sponsorship_community = models.CharField(max_length=250, null=True, blank=True)
    how_you_knew_consolata = models.CharField(max_length=250, null=True, blank=True)
    disability_nature = models.CharField(max_length=250, null=True, blank=True)
    confirm_information = models.CharField(max_length=250, null=True, blank=True)
    non_refundable_fee = models.FileField(upload_to='online-application/', null=True, blank=True)
    copy_of_id = models.FileField(upload_to='online-application/', null=True, blank=True)
    passport_photo = models.ImageField(upload_to='online-application/', null=True, blank=True)
    coppy_of_all_degrees = models.FileField(upload_to='online-application/', null=True, blank=True)
    copies_of_diplomas = models.FileField(upload_to='online-application/', null=True, blank=True)
    recomendation_phone = models.CharField(max_length=250, null=True, blank=True)
    coppy_of_qualifications = models.FileField(upload_to='online-application/', null=True, blank=True)
    coppy_of_transcripts = models.FileField(upload_to='online-application/', null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        managed = True
        db_table = 'tbl_students_admissions'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    

class StudentClassSignIN(models.Model):
    congregation = models.CharField(max_length=250, null=True, blank=True)
    s_no = models.IntegerField(null=True,blank=True)
    reg_no = models.IntegerField(null=True, blank=True)
    student_name = models.CharField(max_length=250, null=True, blank=True)
    sign = models.CharField(max_length=250, null=True, blank=True)
    o_carm = models.CharField(max_length=250, null=True, blank=True)
    svi = models.CharField(max_length=250, null=True, blank=True)
    fdp = models.CharField(max_length=250, null=True, blank=True)
    omi = models.CharField(max_length=250, null=True, blank=True)
    osa = models.CharField(max_length=250, null=True, blank=True)
    ssc = models.CharField(max_length=250, null=True, blank=True)
    mcf = models.CharField(max_length=250, null=True, blank=True)
    cmm = models.CharField(max_length=250, null=True, blank=True)
    cssr = models.CharField(max_length=250, null=True, blank=True)


    
class CourseCodes(models.Model):
    course_code = models.CharField(max_length=100, unique=True)
    course_title = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'tbl_course_codes'

    def __str__(self):
        return f"{self.course_code} - {self.course_title}"
    
class CourseLists(models.Model):
    course_code = models.CharField(max_length=250, unique=True)
    course_title = models.CharField(max_length=250, null=True, blank=True)
    year = models.CharField(max_length=250, null=True, blank=True)
    semester = models.CharField(max_length=250, null=True, blank=True)
    credit = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_course_lists'

    def __str__(self):
        return f"{self.course_code} - {self.semester} {self.year}"



class StudentApplication(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
    ]

    RELIGIOUS_STATUS_CHOICES = [
        ('priest', 'Priest'),
        ('deacon', 'Deacon'),
        ('sister', 'Sister'),
        ('brother', 'Brother'),
        ('seminarian', 'Seminarian'),
        ('none', 'Not Religious'),
    ]

    STUDY_MODE_CHOICES = [
        ('fulltime', 'Full Time'),
        ('parttime', 'Part Time'),
        ('auditing', 'Auditing'),
        ('evening', 'Evening Study'),
        ('weekend', 'Weekend'),
        ('distance', 'Distance Learning'),
    ]

    SCHOOL_APPLIED =[
        ('school of Philosophy', 'School Of Philosophy'),
        ('school of theology', 'School Of Theology'),
        ('school of counselling psychology', 'School Of Counselling Psychology')
    ]

    PROGRAM_APPLIED =[
        ('baccalaureate', 'Baccalaureate'),
        ('bachelor', 'Bachelor'),
        ('diploma', 'Diploma'),
        ('certificate', 'Certificate')
    ]

    ANTICIPATED_DURATION =[
        ('1 year', '1 Year'),
        ('2 years', '2 Years'),
        ('3 years', '3 Years'),
        ('4 years', '4 Years')
    ]

    applicant_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )

    # --- PERSONAL INFO ---
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    citizenship = models.CharField(max_length=100)
    passport_or_id_no = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=10, blank=True, null=True)

    # Religious details
    religious_affiliation = models.CharField(max_length=100, blank=True, null=True)
    religious_status = models.CharField(choices=RELIGIOUS_STATUS_CHOICES, max_length=20, blank=True, null=True)
    diocese = models.CharField(max_length=150, blank=True, null=True)
    congregation = models.CharField(max_length=150, blank=True, null=True)

    # Contacts
    permanent_address = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=False)
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    # Next of kin
    next_of_kin_name = models.CharField(max_length=150, blank=True, null=True)
    next_of_kin_relationship = models.CharField(max_length=100, blank=True, null=True)
    next_of_kin_address = models.TextField(blank=True, null=True)
    next_of_kin_email = models.EmailField(blank=True, null=True)
    next_of_kin_phone = models.CharField(max_length=30, blank=True, null=True)

    # --- PROGRAM INFO ---
    study_mode = models.CharField(max_length=20, choices=STUDY_MODE_CHOICES, blank=True, null=True)
    school_applied = models.CharField(max_length=150, choices=SCHOOL_APPLIED, blank=True, null=True)
    programme_applied = models.CharField(max_length=150, choices=PROGRAM_APPLIED, blank=True, null=True)
    anticipated_duration_years = models.CharField(max_length=150, choices=ANTICIPATED_DURATION, blank=True, null=True)

    studied_before = models.BooleanField(default=False)
    previous_student_id = models.CharField(max_length=50, blank=True, null=True)
    previous_school = models.CharField(max_length=150, blank=True, null=True)
    enrollment_from = models.IntegerField(blank=True, null=True)
    enrollment_to = models.IntegerField(blank=True, null=True)

    # --- SPONSOR / RECOMMENDATION ---
    recommending_authority = models.CharField(max_length=150, blank=True, null=True)
    recommending_organization = models.CharField(max_length=150, blank=True, null=True)
    recommendation_address = models.TextField(blank=True, null=True)
    recommendation_phone = models.CharField(max_length=30, blank=True, null=True)
    recommendation_email = models.EmailField(blank=True, null=True)

    sponsor_name = models.CharField(max_length=150, blank=True, null=True)
    sponsor_type = models.CharField(max_length=100, blank=True, null=True)
    sponsor_address = models.TextField(blank=True, null=True)
    sponsor_phone = models.CharField(max_length=30, blank=True, null=True)
    sponsor_email = models.EmailField(blank=True, null=True)
    sponsor_province = models.CharField(max_length=150, blank=True, null=True)

    # --- OTHER INFO ---
    referral_source = models.CharField(max_length=200, blank=True, null=True)  # How did you know about CIU?
    has_disability = models.BooleanField(default=False)
    nature_of_disability = models.TextField(blank=True, null=True)

    # --- CONSENT ---
    consent_signed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return f"{self.surname} {self.first_name}"


class EducationHistory(models.Model):
    """
    One-to-many education rows linked to StudentApplication.
    type_of_institution can be: primary, secondary, college, seminary, university, other
    """
    INSTITUTION_TYPE_CHOICES = [
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('college', 'College'),
        ('seminary', 'Seminary'),
        ('university', 'University'),
        ('other', 'Other'),
    ]

    application = models.ForeignKey(StudentApplication, related_name='education_rows', on_delete=models.CASCADE)
    institution_type = models.CharField(max_length=20, choices=INSTITUTION_TYPE_CHOICES)
    institution_name = models.CharField(max_length=255)
    from_year = models.IntegerField(blank=True, null=True)
    to_year = models.IntegerField(blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    grade_or_result = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-to_year', 'institution_type']

    def __str__(self):
        return f"{self.institution_type} - {self.institution_name}"


# app/models.py (append)

class ApplicationAttachment(models.Model):
    """
    Stores uploaded files linked to a StudentApplication.
    """
    ATTACHMENT_TYPE_CHOICES = [
        ('fee_receipt', 'Application Fee Receipt'),
        ('id_passport', 'ID / Passport'),
        ('passport_photo', 'Passport Photo'),
        ('degree', 'Degree Certificate'),
        ('transcript', 'Transcript'),
        ('professional', 'Professional Qualification'),
        ('diploma', 'Diploma / Certificate'),
        ('highschool', 'High School Certificate'),
        ('cv', 'Curriculum Vitae'),
        ('recommendation', 'Recommendation Letter'),
        ('letter_of_interest', 'Letter of Interest File'),
        ('other', 'Other'),
    ]

    application = models.ForeignKey('StudentApplication', related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='applications/documents/%Y/%m/%d/')
    attachment_type = models.CharField(max_length=40, choices=ATTACHMENT_TYPE_CHOICES, default='other')
    original_filename = models.CharField(max_length=512, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_attachment_type_display()} - {self.original_filename or self.file.name}"

