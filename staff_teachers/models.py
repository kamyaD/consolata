from django.db import models
from student.models import TblStudentsAdmissions
from django.utils.timezone import now

def get_year_choices():
    current_year = now().year
    return [(year, year) for year in range(2000, current_year + 1)]



# Create your models here.
class TblTeachersPay(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
    education = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    normal_mark1 = models.CharField(max_length=5)
    normal_mark2 = models.CharField(max_length=5)
    special_mark = models.CharField(max_length=5)
    number_normal = models.IntegerField()
    special_number = models.IntegerField()
    onsite_mark = models.CharField(max_length=5)
    onsite_number = models.IntegerField()
    normal_class_hours = models.IntegerField()
    normal_class_total = models.IntegerField()
    afternoon_activity_rate = models.IntegerField()
    activities_hours = models.IntegerField()
    activities_total = models.IntegerField()
    quality_work_rate = models.IntegerField()
    tod_hours = models.IntegerField()
    tod_total = models.IntegerField()
    special_class_rate = models.IntegerField()
    tutored_hours = models.IntegerField()
    tutored_total = models.IntegerField()
    eca_rate = models.IntegerField()
    eca_hours = models.IntegerField()
    eca_total = models.IntegerField()
    meeting_rate = models.IntegerField()
    meeting_number = models.IntegerField()
    meeting_total = models.IntegerField()
    placement_rate = models.IntegerField()
    test_number = models.IntegerField()
    test_total = models.IntegerField()
    internet_total = models.IntegerField()
    normal_class2_rate = models.IntegerField()
    normal2_hours = models.IntegerField()
    normal2_total = models.IntegerField()
    onsite_rate = models.IntegerField()
    onsite_hours = models.IntegerField()
    onsite_total = models.IntegerField()
    salaries = models.IntegerField()
    summation1 = models.IntegerField()
    advance = models.IntegerField()
    advance_total = models.IntegerField()
    charity = models.IntegerField()
    charity_total = models.IntegerField()
    others = models.IntegerField()
    others_total = models.IntegerField()
    summation2 = models.IntegerField()
    gross_total = models.IntegerField()
    date_submitted = models.DateTimeField()
    payment_status = models.CharField(max_length=10)
    approval_status = models.CharField(max_length=50)
    year = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'tbl_teachers_pay'


class TblSchoolInvoice(models.Model):
    invoiceid = models.AutoField(db_column='invoiceID', primary_key=True)  # Field name made lowercase.
    invoice_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    billing_self = models.CharField(max_length=100)
    issue_date = models.DateField()
    due_date = models.DateField()
    language_category = models.CharField(max_length=20)
    language_checkbox = models.CharField(max_length=100)
    computer_category = models.CharField(max_length=20)
    computer_checkbox = models.CharField(max_length=50)
    languages = models.CharField(max_length=20)
    level = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    dollar_rate = models.IntegerField()
    euro_rate = models.IntegerField()
    previous_balance = models.IntegerField()
    balance_ksh_total = models.IntegerField()
    balance_dollar_total = models.IntegerField()
    balance_euro_total = models.IntegerField()
    language_hours = models.IntegerField()
    language_ksh_total = models.IntegerField()
    language_dollar_total = models.IntegerField()
    language_euro_total = models.IntegerField()
    registration_amount = models.IntegerField()
    registration_ksh_total = models.IntegerField()
    registration_dollar_total = models.IntegerField()
    registration_euro_total = models.IntegerField()
    text_book_number = models.IntegerField()
    text_book_amount = models.IntegerField()
    text_book_ksh_total = models.IntegerField()
    text_book_dollar_total = models.IntegerField()
    text_book_euro_total = models.IntegerField()
    activity_fee_amount = models.IntegerField()
    activity_fee_ksh_total = models.IntegerField()
    activity_fee_dollar_total = models.IntegerField()
    activity_fee_euro_total = models.IntegerField()
    id_card_amount = models.IntegerField()
    id_card_ksh_total = models.IntegerField()
    id_card_dollar_total = models.IntegerField()
    id_card_euro_total = models.IntegerField()
    ict_hours = models.IntegerField()
    ict_ksh_total = models.IntegerField()
    ict_dollar_total = models.IntegerField()
    ict_euro_total = models.IntegerField()
    interpretation_hours = models.IntegerField()
    interpretation_amount = models.IntegerField()
    interpretation_ksh_total = models.IntegerField()
    interpretation_dollar_total = models.IntegerField()
    interpretation_euro_total = models.IntegerField()
    translation_hours = models.IntegerField()
    translation_amount = models.IntegerField()
    translation_ksh_total = models.IntegerField()
    translation_dollar_total = models.IntegerField()
    translation_euro_total = models.IntegerField()
    grand_total_ksh_total = models.IntegerField()
    grand_total_dollar_total = models.IntegerField()
    grand_total_euro_total = models.IntegerField()
    discount_amount = models.IntegerField()
    discount_ksh_total = models.IntegerField()
    discount_dollar_total = models.IntegerField()
    discount_euro_total = models.IntegerField()
    effected_payment_amount = models.IntegerField()
    effected_payment_ksh_total = models.IntegerField()
    effected_payment_dollar_total = models.IntegerField()
    effected_payment_euro_total = models.IntegerField()
    overall_balance_ksh_total = models.IntegerField()
    overall_balance_dollar_total = models.IntegerField()
    overall_balance_euro_total = models.IntegerField()
    month = models.CharField(max_length=30)
    invoice_number1 = models.IntegerField()
    payment_status = models.CharField(max_length=10)
    year = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_school_invoice'


class TblRecordSlip(models.Model):
    invoiceid = models.AutoField(db_column='invoiceID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)
    language_from = models.CharField(max_length=50)
    language_to = models.CharField(max_length=50)
    start_date = models.DateField()
    interpretation_hours = models.IntegerField()
    total_interpretation = models.IntegerField()
    proof_read_words = models.IntegerField()
    proof_read_total = models.IntegerField()
    translated_words = models.IntegerField()
    translated_total = models.IntegerField()
    transcription_hours = models.IntegerField()
    transcription_total = models.IntegerField()
    forty_translation = models.IntegerField()
    forty_proof_reading = models.IntegerField()
    forty_interpretation = models.IntegerField()
    forty_transcription = models.IntegerField()
    sixty_translation = models.IntegerField()
    sixty_proof_reading = models.IntegerField()
    sixty_interpretation = models.IntegerField()
    sixty_transcription = models.IntegerField()
    stamp_seal_translation = models.IntegerField()
    stamp_seal_proof_reading = models.IntegerField()
    sub_total_translation = models.IntegerField()
    sub_total_proof_reading = models.IntegerField()
    sub_total_interpretation = models.IntegerField()
    sub_total_transcription = models.IntegerField()
    total_forty_percent = models.IntegerField()
    total_sixty_percent = models.IntegerField()
    level_of_education = models.CharField(max_length=100)
    tuition_amount = models.CharField(max_length=100)
    tuition_hours = models.CharField(max_length=100)
    tuition_total_paid = models.CharField(max_length=100)
    software_service_total = models.CharField(max_length=100)
    ies_total = models.CharField(max_length=100)
    grand_total_ksh = models.IntegerField()
    month = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=10)
    service_payment_status = models.CharField(max_length=10)
    slip_no = models.IntegerField()
    year = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_record_slip'

DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday')
]

class Timetable(models.Model):
    day = models.CharField(max_length=200, choices=DAY_CHOICES, null=True, blank=True)
    year = models.IntegerField()
    from_time = models.CharField(max_length=200, null=True, blank=True)
    to_time = models.CharField(max_length=200, null=True, blank=True)
    lecturer = models.CharField(max_length=250, null=True, blank=True)
    courses = models.CharField(max_length=256, null=True, blank=True)
    room = models.CharField(max_length=100, null=True, blank=True)



SCHOOL_CHOICES = [
    ('School of Theology', 'School of Theology'),
    ('School of Counselling Psychology', 'School Of Counselling Psychology'),
    ('School Of Philosophy', 'School Of Philosophy')
]

QUALIFICATION_CHOICES = [
    ('Baccalaurete','Baccalaurete'),
    ('Bachelor', 'Bachelor'),
    ('Diploma', 'Diploma'),
    ('Certificate', 'Certificate'),
    ('No Award', 'No Award')
]

PHILOSOPHY_COURSE_CHOICES = [
    ('CPH 100', 'Introduction to Philosophy'),
    ('CPH 113.1', 'Cosmology I (Philosophy of Nature)'),
    ('CPH 113.2','Cosmology II (Philosophy of Nature)'),
    ('CPH 180', 'History of Ancient Philosophy')
]

THEOLOGY_COURSE_CHOICES = [
    ('CTBSC 101','Introduction to the Judeo-Christian Scriptures'),
    ('CTCHC 101', 'Church History I: The Early Centuries'),
    ('CTGKL 101','New Testament Greek I'),
    ('CTLTL 101', 'Latin I (afternoon)'),
]

ACADEMIC_YEAR_CHOICES = [
    ('2020-21', '2020-21'),
    ('2021-22', '2021-22'),
    ('2022-23', '2022-23'),
    ('2023-24', '2023-24'),
    ('2025-26', '2025-26'),
    ('2026-27', '2026-27'),
    ('2027-28', '2027-28'),
    ('2028-29', '2028-29'),
    ('2029-30', '2029-30'),
]

MONTH_CHOICES = [
    ("JANUARY", "January"),
    ("FEBRUARY", "February"),
    ("MARCH", "March"),
    ("APRIL", "April"),
    ("MAY", "May"),
    ("JUNE", "June"),
    ("JULLY", "Jully"),
    ("AUGUST", "August"),
    ("SEPTEMBER", "September"),
    ("OCTOBER", "October"),
    ("NOVEMBER", "November"),
    ("DECEMBER", "December"),
]
class TblClaimSheet(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    month = models.CharField(max_length=100, choices=MONTH_CHOICES)
    normal_class = models.CharField(max_length=100)
    normal_time = models.CharField(max_length=100)
    normal_mark = models.CharField(max_length=100)
    normal_number = models.CharField(max_length=100)
    special_class = models.CharField(max_length=100)
    special_time = models.CharField(max_length=100)
    special_mark = models.CharField(max_length=100)
    special_number = models.CharField(max_length=100)
    onsite_class = models.CharField(max_length=100)
    onsite_time = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    date_created = models.CharField(max_length=100)


    class Meta:
        db_table = 'tbl_claim_sheet'
        managed = False  # Since the table already exists in the DB


STATE_CHOICES = [
    ('Registrar Approval', 'Registrar Approval'),
    ('DVC Finance Approval', 'DVC Finance Approval'),
    ('Payment', 'Payment'),
    ('Paid', 'Paid'),

]
class ClaimForm(models.Model):
    """Main form metadata"""
    staff_name = models.CharField(max_length=100, null=True, blank=True)
    staff_email = models.CharField(max_length=100, null=True, blank=True)
    month = models.CharField(max_length=100, choices=MONTH_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    state = models.CharField(max_length=250, choices=STATE_CHOICES, null=True, blank=True)

    @property
    def grand_total(self):
        return sum(item.total for item in self.claimitems.all())


class ClaimItem(models.Model):
    """Row item with calculated total"""
    CATEGORY_CHOICES = [
        ('hours', 'Hours'),
        ('meetings', 'Meetings'),
        ('invigilation_core', 'Invigilation - Core Course'),
        ('invigilation_elective', 'Invigilation - Elective Course'),
        ('marking_cat', 'Marking of CATs'),
        ('marking_exam', 'Marking of Final Exams'),
    ]

    claim_form = models.ForeignKey(ClaimForm, on_delete=models.CASCADE, related_name='claimitems')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=100, blank=True, null=True)  # e.g., "Core course"
    quantity = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.rate

    def __str__(self):
        return f"{self.get_category_display()} - {self.description or ''}"



DAYS = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
]

CLASS_LEVELS = [
    (1, 'Class 1'),
    (2, 'Class 2'),
    (3, 'Class 3'),
]

TIME_SLOTS = [
    ('08:30-09:20', '08:30–09:20'),
    ('09:25-10:15', '09:25–10:15'),
    ('10:30-11:20', '10:30–11:20'),
    ('11:25-12:15', '11:25–12:15'),
    ('14:30-15:30', '14:30–15:30'),
    ('15:30-16:30', '15:30–16:30'),
]

class TimetableEntry(models.Model):
    day = models.CharField(max_length=10, choices=DAYS)
    class_level = models.IntegerField(choices=CLASS_LEVELS)
    course_code_first = models.CharField(max_length=100, null=True, blank=True)
    course_title_first = models.TextField()
    lecturer_first = models.CharField(max_length=100, null=True, blank=True)
    first_room = models.CharField(max_length=20, null=True, blank=True)
    course_code_second = models.CharField(max_length=100, null=True, blank=True)
    course_title_second = models.TextField(null=True, blank=True)
    lecturer_second = models.CharField(max_length=100, null=True, blank=True)
    second_room = models.CharField(max_length=20, null=True, blank=True)
    after_break_course_code_first = models.CharField(max_length=100, null=True, blank=True)
    after_break_course_title_first = models.TextField(null=True, blank=True)
    after_break_lecturer_first = models.CharField(max_length=100, null=True, blank=True)
    after_break_first_room = models.CharField(max_length=20, null=True, blank=True)
    after_break_course_code_second = models.CharField(max_length=100, null=True, blank=True)
    after_break_course_title_second = models.TextField(null=True, blank=True)
    after_break_lecturer_second = models.CharField(max_length=100, null=True, blank=True)
    after_break_second_room = models.CharField(max_length=20, null=True, blank=True)
    after_lunch_course_code_first = models.CharField(max_length=100, null=True, blank=True)
    after_lunch_course_title_first = models.TextField(null=True, blank=True)
    after_lunch_lecturer_first = models.CharField(max_length=100, null=True, blank=True)
    after_lunch_first_room = models.CharField(max_length=100, null=True, blank=True)
    after_lunch_course_code_second = models.CharField(max_length=100, null=True, blank=True)
    after_lunch_course_title_second = models.TextField(null=True, blank=True)
    after_lunch_lecturer_second = models.CharField(max_length=100, null=True, blank=True)
    after_lunch_second_room = models.CharField(max_length=20, null=True, blank=True)
    lecturer = models.CharField(max_length=100, null=True, blank=True)
    time_slot = models.CharField(max_length=100, null=True, blank=True)
    room = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.day} - Class {self.class_level} - {self.time_slot}"



class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    year = models.CharField(max_length=10, choices=ACADEMIC_YEAR_CHOICES, default='2023-24')
    semester = models.CharField(max_length=10, choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2')], default='Semester 1')


    def __str__(self):
        return self.title
    
class CourseResults(models.Model):
    student = models.ForeignKey(
    TblStudentsAdmissions,
    to_field='studentid',  # important!
    db_column='student_id',  # keep consistent with existing DB
    on_delete=models.CASCADE
)

    congregation = models.CharField(max_length=250, null=True, blank=True)
    course_code = models.CharField(max_length=100, null=True, blank=True)
    course_title = models.CharField(max_length=250, null=True, blank=True)
    semester = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=250, choices=[('2024-25', '2024-25', ), ('2025-26', '2025-26'), ('2026-27', '2026-27'), ('2027-28', '2027-28')], default='2024-25')
    marks = models.FloatField(null=True, blank=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    credit = models.FloatField(null=True, blank=True)
    class_no = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        managed = True
        db_table = 'tbl_results'

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course_code}"

class PsychologyRegistration(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    payment_code = models.CharField(max_length=50)
    adm = models.CharField(max_length=20, blank=True, null=True)
    registration_date = models.DateField(default=now)

    class Meta:
        managed = False
        app_label = 'old_website_app'
        db_table = 'tbl_psychology_registration'
        
