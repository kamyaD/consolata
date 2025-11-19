# student/views.py
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import TblStudentsAdmissions, EducationHistory, StudentApplication, ApplicationAttachment
from .forms import StudentCreationForm, StudentUpdateForm,StudentApplicationForm
from staff_teachers.models import CourseResults
from staff_teachers.models import Timetable
from userauth.models import CustomUser
# from .utils import render_to_pdf
from django.db import transaction



def student_list(request):
    return HttpResponse("This is the student list page.")


def fetch_timetable(request):
    template = 'student/student_timetable.html'
    timetables = Timetable.objects.all()
    

    context = {
        'timetables': timetables
    }

    return render(request,template, context)

@login_required
def view_individual_sudent(request):
    template = 'admin/individual_stident.html'

    try:
        student = TblStudentsAdmissions.objects.filter(email=request.user.email).first()
        print("student", student.first_name)

        # Pre-fill the form with student instance data
        form = StudentUpdateForm(instance=student)

        context = {
            'student': student,
            'form': form
        }
        return render(request, template, context)

    except TblStudentsAdmissions.DoesNotExist:
        messages.error(request, "Requested student record does not exist. Please apply here")
        return redirect('student:application_form')


@login_required  
def fetch_student_results(request):
    template = 'student/student_results.html'
    results = CourseResults.objects.filter(student__email=request.user.email)
    
    if not results:
        messages.error(request, "No results found for this student.")
        return redirect('student:get-student-record')

    context = {
        'results': results
    }
    
    return render(request, template, context)


def update_student(request, pk):
    student = get_object_or_404(TblStudentsAdmissions, pk=pk)
    if request.method == "POST":
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student record updated successfully.")
            return redirect("consolata_admin:view-student", pk=student.pk)
    else:
        messages.error(request, "Please fill all the required fields.")
        form = StudentUpdateForm(instance=student)
    
    return render(request, "consolata_admin/student_edit.html", {"form": form, "student": student})






# @ensure_csrf_cookie
def application_form_view(request):
    """
    Render the single-page application form.
    """
    form = StudentApplicationForm()
    return render(request, 'student/application_form.html', {'form': form})

# # app/views.py (relevant imports)
# import json
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse, HttpResponseBadRequest
# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.db import transaction

# from .forms import StudentApplicationForm
# from .models import StudentApplication, EducationHistory, ApplicationAttachment

@require_POST
def application_submit_ajax(request):
    """
    Accepts the form via multipart/form-data (FormData), including files and an 'education_rows' JSON string.
    Saves StudentApplication, related EducationHistory rows, and ApplicationAttachment records.
    """
    # Make POST mutable if we need to pop later
    post = request.POST.copy()
    files = request.FILES

    # Extract education_rows JSON string (sent from client)
    education_rows_raw = post.pop('education_rows', ['[]'])[0]  # QueryDict pop returns list
    try:
        education_rows = json.loads(education_rows_raw)
        if not isinstance(education_rows, list):
            education_rows = []
    except Exception:
        education_rows = []

    # Normalize boolean-like fields
    def to_bool(val):
        if isinstance(val, bool):
            return val
        if val is None:
            return False
        return str(val).lower() in ['true', '1', 'on', 'yes']

    if 'consent_signed' in post:
        post['consent_signed'] = to_bool(post.get('consent_signed'))
    if 'studied_before' in post:
        post['studied_before'] = to_bool(post.get('studied_before'))
    if 'has_disability' in post:
        post['has_disability'] = to_bool(post.get('has_disability'))

    # Bind form (StudentApplicationForm does NOT include attachments — attachments handled separately)
    form = StudentApplicationForm(post, files=None)  # ModelForm uses POST, files only if file fields are on main model
    if form.is_valid():
        try:
            with transaction.atomic():
                application = form.save(commit=False)
                if request.user.is_authenticated:
                    application.applicant_user = request.user
                application.save()

                # Save education history rows
                created_rows = []
                for row in education_rows:
                    inst_type = row.get('institution_type') or 'other'
                    inst_name = (row.get('institution_name') or '').strip()
                    if not inst_name:
                        continue
                    from_year = row.get('from_year') or None
                    to_year = row.get('to_year') or None
                    qualification = (row.get('qualification') or '').strip()
                    grade = (row.get('grade_or_result') or '').strip()
                    try:
                        from_year = int(from_year) if from_year not in (None, '') else None
                    except (ValueError, TypeError):
                        from_year = None
                    try:
                        to_year = int(to_year) if to_year not in (None, '') else None
                    except (ValueError, TypeError):
                        to_year = None

                    eh = EducationHistory.objects.create(
                        application=application,
                        institution_type=inst_type,
                        institution_name=inst_name,
                        from_year=from_year,
                        to_year=to_year,
                        qualification=qualification,
                        grade_or_result=grade
                    )
                    created_rows.append(eh.id)

                # Save attachments from request.FILES using getlist for multi-file inputs
                # Map input names to attachment_type
                file_field_map = {
                    'application_fee_receipt': 'fee_receipt',
                    'id_passport': 'id_passport',
                    'passport_photos': 'passport_photo',
                    'degree_certificates': 'degree',
                    'transcripts': 'transcript',
                    'professional_certificates': 'professional',
                    'diplomas_certificates': 'diploma',
                    'highschool_certificate': 'highschool',
                    'cv_resume': 'cv',
                    'recommendation_letters': 'recommendation',
                    'letter_of_interest_file': 'letter_of_interest',
                }

                created_attachments = []
                for input_name, att_type in file_field_map.items():
                    # If multiple allowed -> getlist()
                    if input_name in ['passport_photos', 'degree_certificates', 'transcripts', 'professional_certificates', 'diplomas_certificates', 'recommendation_letters']:
                        file_list = request.FILES.getlist(input_name)
                    else:
                        # Single file field
                        file_obj = request.FILES.get(input_name)
                        file_list = [file_obj] if file_obj else []

                    for f in file_list:
                        ApplicationAttachment.objects.create(
                            application=application,
                            file=f,
                            attachment_type=att_type,
                            original_filename=getattr(f, 'name', '')
                        )

                # Also store letter_of_interest_text if present on form fields (StudentApplication model should have it)
                # If your StudentApplication has letter_of_interest_text, the form saved it already.

                # Return success + redirect
                messages.success(request, "Application submitted successfully.")
                return JsonResponse({
                    'status': 'success',
                    'message': 'Application submitted successfully.',
                    'application_id': application.id,
                    'created_education_rows': created_rows,
                    'created_attachments': created_attachments,
                    'redirect_url': '/'  # homepage redirect
                }, status=201)

        except Exception as e:
            import traceback
            print("🔥 ERROR TRACEBACK 🔥")
            traceback.print_exc()  # ✅ FULL TRACE IN TERMINAL
            return JsonResponse({
                'status': 'error',
                'message': f'Failed to save application: {str(e)}'
            }, status=500)

    else:
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        }, status=400)


def applicants_list_view(request):
    applicants = StudentApplication.objects.all().order_by('-created_at')  # latest first
    return render(request, 'student/applicants_list.html', {'applicants': applicants})


def applicant_detail_view(request, application_id):
    application = get_object_or_404(StudentApplication, id=application_id)
    education_history = EducationHistory.objects.filter(application=application)

    return render(request, 'student/applicant_detail.html', {
        'application': application,
        'education_history': education_history
    })