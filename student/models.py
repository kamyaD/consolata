from django.db import models
from django.utils.timezone import now
from userauth.models import CustomUser


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
    ('4 Months', '4 Months')
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
    admission_year = models.CharField(max_length=20, choices=get_year_choices(), default=now().year)
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






        
   