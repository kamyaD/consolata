from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import (TblTeachersPay, TblSchoolInvoice,TblRecordSlip, ClaimForm, ClaimItem,
                    Timetable, TblClaimSheet, TimetableEntry, CourseResults,PsychologyRegistration)
from student.models import StudentClassSignIN, TblStudentsAdmissions,CourseLists
from student.utils import render_to_pdf
from .forms import TblClaimSheetForm, ClaimFormForm, TimetableEntryForm, PsychologyRegistrationForm
from django.core.mail import send_mass_mail, EmailMessage,get_connection
import datetime
import csv
import io
from datetime import datetime

import tempfile, os
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from .forms import CourseCSVUploadForm, CourseEditForm
from django.utils.timezone import now
from collections import defaultdict
from django.conf import settings
import time




# Create your views here.
@login_required
def view_teachers_pay(request):
    template = 'staff/pay_update.html'
    teachers = TblTeachersPay.objects.all()

    for teacher in teachers:
        teacher.name = f"{teacher.first_name} {teacher.last_name}" 

    # form = StudentCreationForm()

    context = {
        'teachers': teachers,
        # 'form': form
    }

    return render(request,template,context)

@login_required
def admin_office(request):
    template = 'staff/admin_office.html'
    school_invoices = TblSchoolInvoice.objects.all()
    record_slips = TblRecordSlip.objects.all()

    context = {
        'school_invoices': school_invoices,
        'record_slips': record_slips
    }

    return render(request,template,context)



def create_timetable(request):
    if request.method == 'POST':
        form = TimetableEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Timetable entry created successfully.")
            return redirect('staff_teachers:timetable')
        else:
            messages.error(request, "There were errors in your form. Please review and submit again.")
    else:
        template = 'staff/timetable.html'

        # Get today's day name (e.g. 'Monday')
        today = datetime.today().strftime('%A')


        # Only fetch records for today if it's a weekday
        if today in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            tables = TimetableEntry.objects.all()
        
        else:
            tables = TimetableEntry.objects.all()  # Return empty QuerySet for weekends

        form = TimetableEntryForm()
        

        return render(request, template, {'tables': tables, 'form':form})

    
def edit_time_table(request, id=None):
    if request.method == 'POST':
        table = Timetable.objects.get(pk=id)
        post = request.POST
        table.day = post.get('day')
        table.year = post.get('class')
        table.from_time = post.get('from_time')
        table.to_time = post.get('to_time')
        table.lecturer = post.get('lecturer')
        table.courses = post.get('courses')
        table.room = post.get('room')
        table.save()
        messages.success(request,"Time table updated Successfully")

        return redirect('staff_teachers:timetable')
    
    template='staff/edit_timetable.html',
    table = Timetable.objects.get(pk=id)
    form = TimetableForm()
    context = {'table': table, 'form': form}

    return render(request, template, context)

def delete_timetable_raw(request, id):
    table = table = Timetable.objects.get(pk=id)
    table.delete()
    return redirect('staff_teachers:timetable')

def fetch_student_class_sign(request):
    template = 'staff/class_sign.html'
    signs = StudentClassSignIN.objects.all()

    context = {
        'signs': signs
    }
    return render(request, template, context)
    



def generate_timetable_pdf(request):
    # Fetch all timetable records
    tables = TimetableEntry.objects.all()

    # Render the HTML template as a string
    html_string = render_to_string('staff/timetable_pdf.html', {'tables': tables})

    # Create response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="timetable.pdf"'

    # Create temporary file for WeasyPrint
    with tempfile.NamedTemporaryFile(delete=True, suffix='.pdf') as output:
        HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(
            target=output.name,
            stylesheets=[CSS(string='''
                @page {
                    size: A4 landscape;
                    margin: 1cm;
                }
                body {
                    font-family: 'Arial', sans-serif;
                    font-size: 11px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid #ccc;
                    padding: 5px;
                    text-align: left;
                }
                .flex {
                    display: flex;
                    justify-content: space-between;
                    gap: 0.5rem;
                    flex-wrap: wrap;
                }
                hr {
                    border: none;
                    border-top: 1px solid #ccc;
                    margin: 4px 0;
                }
            ''')]
        )
        output.seek(0)
        response.write(output.read())

    return response

# def generate_timetable_pdf(request):
#     tables = TimetableEntry.objects.all()
#     html_string = render_to_string('staff/timetable_pdf.html', {'tables': tables})

#     font_path = os.path.join(settings.BASE_DIR, 'yourapp', 'static', 'fonts', 'DejaVuSans.ttf')

#     css = CSS(string=f"""
#         @font-face {{
#             font-family: 'CustomFont';
#             src: url('file://{font_path}');
#         }}
#         @page {{
#             size: A4 landscape;
#             margin: 1cm;
#         }}
#         body {{
#             font-family: 'CustomFont';
#             font-size: 11px;
#         }}
#         table {{
#             width: 100%;
#             border-collapse: collapse;
#         }}
#         th, td {{
#             border: 1px solid #ccc;
#             padding: 5px;
#             text-align: left;
#         }}
#         .flex {{
#             display: flex;
#             justify-content: space-between;
#             gap: 0.5rem;
#             flex-wrap: wrap;
#         }}
#         hr {{
#             border: none;
#             border-top: 1px solid #ccc;
#             margin: 4px 0;
#         }}
#     """)

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="timetable.pdf"'

#     with tempfile.NamedTemporaryFile(delete=True, suffix='.pdf') as output:
#         HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(
#             target=output.name,
#             stylesheets=[css]
#         )
#         output.seek(0)
#         response.write(output.read())

#     return response

def generate_claim_form(request):
    template = 'staff/claim_sheet.html'
    sheets = TblClaimSheet.objects.all()
    form = TblClaimSheetForm()

    context = {
        'sheets': sheets,
        'form':form
    }

    return render(request, template, context)

def create_claim(request):
    if request.method=='POST':
        post = request.POST

        claim = TblClaimSheet.objects.create(
            name = post.get('name'),
            language =post.get('language'),
            month = post.get('month'),
            normal_class = post.get('normal-class'),
            normal_time = post.get('normal-time'),
            normal_mark = post.get('normal-mark'),
            normal_number = post.get('normal-number'),
            special_class = post.get('special-class'),
            special_time = post.get('special-time'),
            special_mark = post.get('special-mark'),
            special_number = post.get('special-number'),
            onsite_class = post.get('onsite-class'),
            onsite_time = post.get('onsite-time'),
            level = post.get('level'),
            date_created = post.get('date-created')
        )
        messages.success(request, "Claim form created successfully.")
        return redirect('staff_teachers:claim-form')


def create_staff_claim_form(request):
    if request.method == 'POST':
        staff_name = request.POST.get('staff_name')
        month = request.POST.get('month')
        comments = request.POST.get('comments')
        grand_total = request.POST.get('grand-total-input')

        
        claim_form = ClaimForm.objects.create(
            staff_name=staff_name,
            staff_email = request.user.email,
            month=month,
            comments=comments,
            total = grand_total,
            state = 'Registrar Approval'
        )

        # Extract dynamic items
        categories = request.POST.getlist('category[]')
        descriptions = request.POST.getlist('description[]')
        quantities = request.POST.getlist('quantity[]')
        rates = request.POST.getlist('rate[]')

        for i in range(len(categories)):
            try:
                ClaimItem.objects.create(
                    claim_form=claim_form,
                    category=categories[i],
                    description=descriptions[i],
                    quantity=int(quantities[i]),
                    rate=float(rates[i])
                )
            except Exception as e:
                print(f"Skipping item due to error: {e}")

        messages.success(request, "Claim form submitted successfully.")
        return redirect('staff_teachers:claim-form-detail')
    
    form = ClaimFormForm()
    context = {'user':request.user, 'form':form}
    return render(request, 'staff/staff_claim_form_create.html', context)


def view_claim_staff_form(request, pk):
    form = get_object_or_404(ClaimForm, pk=pk)
    items = form.claimitems.all()

    return render(request, 'staff/claim_form_view.html', {
        'form': form,
        'items': items
    })


def view_individual_claims(request):
    template = 'staff/claim_form_detail.html'
    claims = ClaimForm.objects.filter(staff_email=request.user.email )
    context = {
        'claims': claims
    }

    return render(request, template, context)

def view_all_claims(request, id=None):
    template = 'staff/all_claims.html'
    claims = ClaimForm.objects.all()
    context = {
        'claims': claims
    }
    
    if id:
        claim = ClaimForm.objects.get(pk=id)
        claim_items = ClaimItem.objects.filter(claim_form__id=id)
        if request.method == 'POST':
            post = request.POST
            claim.staff_name = post.get('staff_name')
            claim.month = post.get('month')
            claim.comments = post.get('comments')
            claim.total = post.get('grand-total-input')
            claim.save()
            
            # Get claim item fields from POST
            categories = request.POST.getlist('category[]')
            descriptions = request.POST.getlist('description[]')
            quantities = request.POST.getlist('quantity[]')
            rates = request.POST.getlist('rate[]')

            # Loop through and update each ClaimItem
            for i, item in enumerate(claim_items):
                item.category = categories[i]
                item.description = descriptions[i]
                item.quantity = int(quantities[i])
                item.rate = float(rates[i])
                item.save()

        else:
            template = 'staff/edit_claim_form.html'
            
            for item in claim_items:
                print("category", item.category)
                print("category", item.description)
            context = {
                'claim': claim,
                'claim_items': claim_items
            }
            return render(request, template, context)
        

    return render(request, template, context)


@login_required
def claim_form_approval_view(request, id):
    if request.user.role == 'Registrar':
        claim = ClaimForm.objects.get(state='Registrar Approval', pk=id)

        print("claim===>",claim)


        # Prevent access if already past registrar stage
        if claim.state != 'Registrar Approval':
            messages.warning(request, "This claim is not pending registrar approval.")
            return redirect('staff_teachers:all-claims')  # adjust redirect

        if request.method == 'POST':
            print("here==>")
            # Mark as approved by registrar
            claim.state = 'DVC Finance Approval'
            claim.save()
            print("claim state===>", claim.state)
            messages.success(request, "Claim approved and sent to Dean.")
            return redirect('staff_teachers:all-claims')  # adjust

        return render(request, 'staff/all_claims.html', {'claim': claim})
    
    if request.user.role == 'DVC Finance':
        claim = ClaimForm.objects.get(state='DVC Finance Approval', pk=id)

        print("claim===>",claim)

        # Prevent access if already past dean stage
        if claim.state != 'DVC Finance Approval':
            messages.warning(request, "This claim is not pending Dean's approval.")
            return redirect('staff_teachers:all-claims')  # adjust redirect

        if request.method == 'POST':
            print("here==>")
            # Mark as approved by registrar
            claim.state = 'Payment'
            claim.save()
            print("claim state===>", claim.state)
            messages.success(request, "Claim approved and sent to Finance Controller.")
            return redirect('staff_teachers:all-claims')  # adjust
        
        return render(request, 'staff/all_claims.html', {'claim': claim})
    
    if request.user.role == 'Finance Administrator':
        claim = ClaimForm.objects.get(state='Payment', pk=id)


        # Prevent access if already past registrar stage
        if claim.state != 'Payment':
            messages.warning(request, "This claim is not pending Finance Administrator approval.")
            return redirect('staff_teachers:all-claims')  # adjust redirect

        if request.method == 'POST':
            print("here==>")
            # Mark as approved by registrar
            claim.state = 'Paid'
            claim.save()
            print("claim state===>", claim.state)
            messages.success(request, "Claim approved and Paid.")
            return redirect('staff_teachers:all-claims')  # adjust

        return render(request, 'staff/all_claims.html', {'claim': claim})


def normalize_header(header):
    return header.lower().strip().replace(" ", "_")

def find_course_code(course_title):
    course_title = course_title.strip().title()
    course = CourseLists.objects.filter(course_title__iexact=course_title).first()
    return {
        "code": course.course_code if course else None,
        "credit": course.credit if course else None,
        "semester": course.semester if course else None,
        "class": course.year if course else None
    }

def compute_grade(marks):
    if marks >= 70:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 45:
        return 'D'
    elif marks >= 40:
        return 'E'
    else:
        return 'F'





def normalize_header(header):
    return header.strip().lower().replace(" ", "_").replace(".", "")


def upload_results_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if not csv_file or not csv_file.name.endswith('.csv'):
            messages.error(request, "Please upload a valid CSV file.")
            return render(request, 'upload_predictions.html')

        try:
            decoded_file = csv_file.read().decode('utf-8-sig')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)

            headers = [normalize_header(h) for h in next(reader)]
            print("headers===>", headers)
            reader = csv.DictReader(io_string, fieldnames=headers)

            static_fields = {'cong', 's_no', 'regno', 'student_name', 'semester', 'year', 'class'}
            saved_rows = 0
            skipped_rows = 0

            for row in reader:
                row = {k.strip(): v.strip() for k, v in row.items()}
                reg_no = row.get('regno', '')
    
                name = row.get('student_name', '')
                
                congregation = row.get('cong', '')
                semester = row.get('semester', '')
                
                year = row.get('year', '') or '2024-25'
                class_no = row.get('class', '')
                

                # Skip invalid reg_no or name
                if not reg_no or not name:
                    skipped_rows += 1
                    continue

                # Clean reg_no (e.g., from 3003.0)
                try:
                    reg_no = str(int(float(reg_no)))
                except ValueError:
                    skipped_rows += 1
                    continue

                # Parse name parts
                name_parts = name.strip().split()
                first_name = name_parts[0]
                last_name = name_parts[-1] if len(name_parts) > 1 else ''
                other_names = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ''

                # Find or create student
                student = TblStudentsAdmissions.objects.filter(registration_number__iexact=reg_no).first()
                if not student:
                    student = TblStudentsAdmissions.objects.create(
                        registration_number=reg_no,
                        first_name=first_name,
                        last_name=last_name,
                        other_names=other_names,
                        congregation=congregation,
                    )

                for key, value in row.items():
                    if key in static_fields or not value:
                        continue

                    course_title = key.replace('_', ' ').title()

                    # Skip invalid marks
                    try:
                        marks = float(value)
                    except ValueError:
                        skipped_rows += 1
                        continue

                    course_data = find_course_code(course_title)
                    course_code = course_data.get('code')
                    credit = course_data.get('credit')
                    
                    if not course_code or credit is None:
                        skipped_rows += 1
                        continue

                    # Check for existing result
                    exists = CourseResults.objects.filter(
                        student=student,
                        course_code=course_code,
                        semester=semester,
                        year=year,
                        class_no = class_no,
                    ).exists()
                    if exists:
                        skipped_rows += 1
                        continue

                    # Save result
                    CourseResults.objects.create(
                        student=student,
                        congregation=congregation,
                        course_code=course_code,
                        course_title=course_title,
                        semester=semester,
                        year=year,
                        marks=marks,
                        grade=compute_grade(marks),
                        credit=credit,
                        class_no=class_no,

                    )
                    saved_rows += 1

            messages.success(
                request,
                f"✅ Upload complete: {saved_rows} results saved, {skipped_rows} rows skipped."
            )

        except Exception as e:
            messages.error(request, f"❌ Error processing CSV file: {e}")

        return redirect('staff_teachers:view-results')

def edit_result(request, id):
    result = get_object_or_404(CourseResults, pk=id)

    if request.method == 'POST':
        semester = request.POST.get('semester')
        year = request.POST.get('year')
        course_code = request.POST.get('course_code')
        credit= request.POST.get('credit')
        print("credit===>", credit)
        congregation = request.POST.get('congregation') 
        marks = request.POST.get('marks')
        if marks:
            try:
                marks = float(marks)
                result.congregation = congregation
                result.credit = credit
                result.course_code = course_code
                result.year = year
                result.semester = semester
                result.marks = marks
                result.grade = compute_grade(marks)
                result.save()
                messages.success(request, "Result updated successfully.")
                return redirect('staff_teachers:view-results')
            except ValueError:
                messages.error(request, "Please enter a valid response.")
        else:
            messages.error(request, "Marks cannot be empty.")
        return redirect('staff_teachers:view-results')

    return render(request, 'staff/edit_result.html', {'result': result})

def upload_course_list(request):
    if request.method == 'POST':
        form = CourseCSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            decoded_file = file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)

            created = 0
            updated = 0

            for row in reader:
                course_code = row.get('Course Code')
                course_title = row.get('Course Title')
                credit = row.get('Credits')
                print("credit===>", credit)
                year = row.get('Year')
                semester = row.get('Semester')

                if course_code:
                    obj, created_obj = CourseLists.objects.update_or_create(
                        course_code=course_code.strip(),
                        defaults={
                            'course_title': course_title.strip() if course_title else '',
                            'year': year.strip() if year else '',
                            'semester': semester.strip() if semester else '',
                            'credit': credit.strip() if credit else 0,
                        }
                    )
                    if created_obj:
                        created += 1
                    else:
                        updated += 1

            messages.success(request, f"{created} courses created, {updated} updated.")
            return redirect('staff_teachers:view-course-list')
    else:
        form = CourseCSVUploadForm()
    return render(request, 'staff/upload_course.html', {'form': form})

def view_all_courses(request):
    courses = CourseLists.objects.all() 
    return render(request, 'staff/course_list.html', {'courses': courses})

def edit_course_list(request, id):
    course = get_object_or_404(CourseLists, pk=id)

    if request.method == 'POST':
        form = CourseEditForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully.")
            return redirect('staff_teachers:view-course-list')
        else:
            print(form.errors)  # Debugging
    else:
        form = CourseEditForm(instance=course)

    return render(request, 'staff/course_list.html', {'form': form})




def show_exam_results(request):
    template = 'staff/show_results.html'
    results = CourseResults.objects.all()
    
    context = {
        'results': results
    }

    return render(request, template, context)

def create_course_list(request):
    if request.method == 'POST':
        form = CourseEditForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course created successfully.")
            return redirect('staff_teachers:view-course-list')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "There were errors in your form. Please review and submit again.")
    else:
        form = CourseEditForm()

    return render(request, 'staff/create_course.html', {'form': form})




def compute_class_awarded(average):
    if average >= 70:
        return "First Class Honours"
    elif average >= 60:
        return "Upper Second Class Honours"
    elif average >= 50:
        return "Lower Second Class Honours"
    elif average >= 45:
        return "Adequate Pass"
    elif average >= 40:
        return "Bare Pass"
    else:
        return "Fail"

def populate_transcript(request, student_id):
    template = 'staff/student_transcript.html'
    student = get_object_or_404(TblStudentsAdmissions, pk=student_id)
    results = CourseResults.objects.filter(student=student).order_by('year', 'semester')

    # Group results by semester
    semester_dict = defaultdict(list)
    for result in results:
        key = f"Year:{result.year}  Semester:{result.semester}"
        semester_dict[key].append(result)

    semester_data = []
    total_score = 0
    total_credits = 0

    for sem, courses in semester_dict.items():
        course_data = []
        sem_score = 0
        sem_credits = 0

        for course in courses:
            credit = course.credit or 0
            score = course.marks or 0

            course_data.append({
                'course': course
            })
            sem_score += score * credit
            sem_credits += credit

        avg = round(sem_score / sem_credits, 2) if sem_credits > 0 else 0
        semester_data.append({
            'semester': sem,
            'courses': course_data,
            'average': avg
        })

        total_score += sem_score
        total_credits += sem_credits

    overall_avg = round(total_score / total_credits, 2) if total_credits > 0 else 0

    context = {
        'student': student,
        'semester_data': semester_data,
        'summary': {
            'overall_average': overall_avg,
            'accumulated_credits': total_credits,
            'class_awarded': compute_class_awarded(overall_avg),
            'award_date': now()
        },
        'now': now(),
    }
    return render(request, template, context)



def generate_transcript_pdf(request, student_id):
    student = get_object_or_404(TblStudentsAdmissions, pk=student_id)
    results = CourseResults.objects.filter(student=student).order_by('year', 'semester')

    semester_dict = defaultdict(list)
    for result in results:
        key = f"Year:{result.year}  Semester:{result.semester}"
        semester_dict[key].append(result)

    semester_data = []
    total_score = 0
    total_credits = 0

    for sem, courses in semester_dict.items():
        course_data = []
        sem_score = 0
        sem_credits = 0

        for course in courses:
            credit = course.credit or 0
            score = course.marks or 0

            course_data.append({'course': course})
            sem_score += score * credit
            sem_credits += credit

        avg = round(sem_score / sem_credits, 2) if sem_credits > 0 else 0
        semester_data.append({
            'semester': sem,
            'courses': course_data,
            'average': avg
        })

        total_score += sem_score
        total_credits += sem_credits

    overall_avg = round(total_score / total_credits, 2) if total_credits > 0 else 0

    context = {
        'student': student,
        'semester_data': semester_data,
        'summary': {
            'overall_average': overall_avg,
            'accumulated_credits': total_credits,
            'class_awarded': compute_class_awarded(overall_avg),
            'award_date': now()
        },
        'now': now(),
        'request': request,
        'logo_url': request.build_absolute_uri(static('img/new_logo.png')),
    }

    html_string = render_to_string('staff/student_transcript_pdf.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))

    result = tempfile.NamedTemporaryFile(delete=True)
    html.write_pdf(result.name)

    with open(result.name, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'filename=transcript_{student.registration_number}.pdf'
        return response


def language_portal(request):
    pass

def clc_claim_form(request):
    template = 'staff/clc_pay_form.html'
    # claims = ClaimForm.objects.filter(staff_email=request.user.email)
    form = ClaimFormForm()

    context = {
        # 'claims': claims,
        'form': form
    }

    return render(request, template, context)

@login_required
def psychology_list(request):
   
    registrations = (
        PsychologyRegistration.objects
        .all()
        .order_by('-registration_date')
    )

    context = {'registrations': registrations}
    return render(request, 'old_website_app/psychology_list.html', context)


def psychology_register(request):
    if request.method == 'POST':
        form = PsychologyRegistrationForm(request.POST)
        if form.is_valid():
            # Save to the old_website database
            instance= form.save()
            
            messages.success(request, f"Registration for {instance.name} was successful!")
            return redirect('staff_teachers:psychology_register')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PsychologyRegistrationForm()

    return render(request, 'old_website_app/psychology_register.html', {'form': form})

@login_required
def send_bulk_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        attachment = request.FILES.get('attachment')
        from_email = 'info@ciu.ac.ke'

        # Get all valid student emails
        students = list(
            PsychologyRegistration.objects.filter(email__isnull=False)
            .exclude(email__exact='')
        )

        total_students = len(students)
        sent_count = 0
        batch_size = 100

        # Use one connection for efficiency
        connection = get_connection(
            username='apikey',
            password=settings.EMAIL_HOST_PASSWORD,
            fail_silently=False,
            timeout=3600  # 1 hour timeout
        )

        for i in range(0, total_students, batch_size):
            batch = students[i:i + batch_size]
            emails = []

            for student in batch:
                email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=from_email,
                    to=[student.email],
                    connection=connection
                )

                if attachment:
                    attachment.open('rb')
                    email.attach(attachment.name, attachment.read(), attachment.content_type)
                    attachment.close()

                emails.append(email)

            try:
                sent = connection.send_messages(emails)
                sent_count += sent or 0
                print(f"Sent batch {i//batch_size + 1}: {sent or 0} emails")
            except Exception as e:
                print(f"Error sending batch {i//batch_size + 1}: {e}")
                # Optional: wait a bit before retrying
                time.sleep(2)

        messages.success(request, f"Bulk emails sent successfully to {sent_count} recipients out of {total_students}.")
        return redirect('staff_teachers:psychology_list')

    return render(request, 'old_website_app/psychology_list.html')