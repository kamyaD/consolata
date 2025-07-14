from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import (TblTeachersPay, TblSchoolInvoice,TblRecordSlip, ClaimForm, ClaimItem,
                    Timetable, PhilosophystudentsResults, Course, CourseLists, TblClaimSheet, TimetableEntry, TranscriptEntry)
from student.models import StudentClassSignIN, TblStudentsAdmissions
from student.utils import render_to_pdf
from .forms import TblClaimSheetForm, ClaimFormForm, TimetableEntryForm
import datetime
import csv
import io
from datetime import datetime

from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile
from collections import defaultdict
from decimal import Decimal, InvalidOperation


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
    


def normalize_header(header):
    return header.strip().lower().replace(" ", "_")



def normalize_header(header):
    return header.lower().replace(' ', '_').replace('.', '')

def upload_results_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "Upload a valid CSV file.")
            return redirect('your-upload-url')

        decoded_file = csv_file.read().decode('utf-8-sig')
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        headers = next(reader)
        normalized_headers = [normalize_header(h) for h in headers]

        io_string.seek(0)
        next(reader)  # skip header row again

        saved_rows = 0
        skipped_rows = 0

        for row in csv.DictReader(io_string, fieldnames=normalized_headers):
            reg_no = row.get('regno')
            student_name = row.get('student_name')
            year = row.get('year')
            school = row.get('school')
            s_no = row.get('sno') or row.get('s_no')
            congregation = row.get('cong')
            credit = row.get('credit')
            semester = row.get('semester')
            course_code = row.get('course_code')

            if not reg_no or not student_name or not year:
                skipped_rows += 1
                continue

            # Split student name
            name_parts = student_name.strip().split()
            first_name = name_parts[0]
            last_name = name_parts[-1]
            other_names = ' '.join(name_parts[1:-1]) if len(name_parts) > 2 else ''

            student, _ = TblStudentsAdmissions.objects.get_or_create(
                registration_number=reg_no.strip(),
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'other_names': other_names,
                    'date_of_birth': '2000-01-01'
                }
            )

            # Loop through all course title columns (from 9th column onward)
            for course_title in normalized_headers[9:]:
                mark = row.get(course_title, '').strip()
                if not mark:
                    continue

                # Create or get course
                course, _ = Course.objects.get_or_create(
                    title=course_title.replace('_', ' ').title(),
                    code=course_code,
                    defaults={
                        'credit': float(credit) if credit else None,
                        'year': int(year),
                        'semester': int(semester) if semester else None,
                        'school': school,
                        'marks': mark,
                    }
                )

                # Link student to course with mark
                PhilosophystudentsResults.objects.create(
                    student=student,
                    course=course,
                    s_no=s_no,
                    congregation=congregation,
                )

                saved_rows += 1

        messages.success(request, f"{saved_rows} results uploaded. {skipped_rows} rows skipped.")
        return redirect('staff_teachers:results')

    return render(request, 'staff/show_results.html')



def show_exam_results(request):
    template = 'staff/show_results.html'
    results = PhilosophystudentsResults.objects.all()

    context = {
        'results': results
    }

    return render(request, template, context)

def fetch_individual_results(request, reg_no):
    template = 'staff/individual_results.html'
    print("reg_no===>",reg_no)
    results = PhilosophystudentsResults.objects.all()
    results = results.filter(student__registration_number = reg_no)
    date_today = datetime.now().strftime("%A, %B %d, %Y")
    
    context = {
        'results': results,
        'date_today': date_today
    }

    return render(request, template, context)

def upload_course_lists(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "Upload a valid CSV file.")
            return redirect('your-upload-url')

        decoded_file = csv_file.read().decode('utf-8-sig')
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        headers = next(reader)
        saved_rows = 0
        skipped_rows = 0

        normalized_headers = [normalize_header(h) for h in headers]

        for row in csv.DictReader(io_string, fieldnames=normalized_headers):
            year = row.get('year')
            semester = row.get('semester')
            course_code = row.get('course_code')
            course_title = row.get('course_title')
            credit = row.get('credits')
            school = row.get('school')

            course = CourseLists.objects.create(
                year = year,
                semester = semester,
                course_code = course_code,
                course_title = course_title,
                credit = credit,
                school = school       
            )

            saved_rows +=1


        messages.success(request, f"{saved_rows} Results uploaded successfully.")
        return redirect('staff_teachers:course-list')
    template = 'staff/show_course_list.html'
    return render(request, template)

def show_course_list(request):
    template = 'staff/show_course_list.html'
    course_lists = CourseLists.objects.all()

    context = {
        'course_lists': course_lists
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
    
    if request.user.role == 'Finance Controller':
        claim = ClaimForm.objects.get(state='Payment', pk=id)


        # Prevent access if already past registrar stage
        if claim.state != 'Payment':
            messages.warning(request, "This claim is not pending Finance Controller approval.")
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
    


def student_transcript_view(request, reg_no):
    student = get_object_or_404(TblStudentsAdmissions, registration_number__iexact=reg_no)

    # Fetch and prefetch related data
    entries = PhilosophystudentsResults.objects.filter(student=student).select_related(
        'course'
    ).order_by('course__year', 'course__semester')

    # Group by (year, semester) tuple
    grouped = defaultdict(list)
    for entry in entries:
        course = entry.course
        year = course.year or 0
        semester = course.semester or 0
        key = (year, semester)
        grouped[key].append(entry)

    semester_data = []
    for (year, semester), courses in grouped.items():
        total_score = Decimal("0.00")
        total_credits = Decimal("0.00")

        for c in courses:
            course = c.course
            try:
                marks = Decimal(course.marks)
                credit = course.credit or Decimal("0")
                total_score += marks * credit
                total_credits += credit
            except (InvalidOperation, AttributeError):
                continue

        avg = (total_score / total_credits).quantize(Decimal("0.01")) if total_credits else Decimal("0.00")
        semester_data.append({
            "semester": f"{year} Semester {semester}",
            "courses": courses,
            "average": avg
        })

    # Sort just in case keys weren't strictly ordered
    semester_data.sort(key=lambda x: (int(x["semester"].split()[0]), int(x["semester"].split()[-1])))

    # Fetch transcript summary if available
    summary = getattr(student, 'transcriptsummary', None)

    return render(request, 'staff/student_transcript.html', {
        "student": student,
        "semester_data": semester_data,
        "summary": summary,
    })

