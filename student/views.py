# student/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TblStudentsAdmissions
from .forms import StudentCreationForm
from staff_teachers.models import Timetable
from .utils import render_to_pdf



def student_list(request):
    return HttpResponse("This is the student list page.")



def online_application(request):
    template ='student/online-application.html'
    form = StudentCreationForm()
    context = {
        'form':form
    }
    return render(request,template, context)
    

def submit_online_application(request):
    if request.method == 'POST':
        post = request.POST
        files = request.FILES

        application = TblStudentsAdmissions.objects.create(
            sir_name = post.get('sir-name'),
            first_name = post.get('first-name'),
            other_names = post.get('other-names'),
            gender = post.get('gender'),
            date_of_birth = post.get('birth-date'),
            birth_place = post.get('place-of-birth'),
            marital_status = post.get('marital-status'),
            religion = post.get('religion'),
            diocese = post.get('diocese'),
            id_passport = post.get('passport'),
            congregation = post.get('congregation'),
            contact = post.get('permanent-address'),
            email = post.get('email'),
            telephone = post.get('phone'),
            next_of_kin = post.get('next-of-kin'),
            next_of_kin_address = post.get('next-of-kin-address'),
            next_of_kin_email = post.get('next-of-kin-email'),
            next_of_kin_phone = post.get('next-of-kin-phone'),
            registration_status = post.get('registration_status'),
            school = post.get('school'),
            school_of_philosophy = post.get('philosophy-school'),
            school_of_theology = post.get('theology-school'),
            school_of_counselling = post.get('counselling-school'),
            anticipated_program_duration = post.get('program-duration'),
            ever_studied_at_ciu = post.get('ever-studied-at-ciu'),
            previous_stud_id = post.get('previous-stud-id'),
            previous_ciu_school = post.get('previous-ciu-school'),
            previous_from_year = post.get('from'),
            prev_to_year = post.get('to'),
            colleges_attended = post.get('colleges-attended'),
            high_school_attended = post.get('high-school-attended'),
            recommending_authority = post.get('recommending-authority'),
            recommending_congregation = post.get('recommending-congregation'),
            sponsor_phone = post.get('sponsorship-phone'),
            sponsor_email = post.get('sponsor-email'),
            how_fee_will_be_paid = post.get('how-fee-will-be-paid'),
            sponsor = post.get('sponsor'),
            sponsor_recomendation = post.get('recomendation-sponsor'),
            recomendation_address = post.get('recomendation-address'),
            recomendation_phone = post.get('recomendation-phone'),
            recomendation_email = post.get('recomendation-email'),
            sponsorship_community = post.get('sponsorship-community'),
            how_you_knew_consolata = post.get('how-you-knew-consolata'),
            disability = post.get('disability'),
            disability_nature = post.get('disability-nature'),
            confirm_information = post.get('confirm-information'),
            non_refundable_fee = files.get('non-refundable-fee'),  # file field
            copy_of_id = files.get('copy-of-id'),                   # file field
            passport_photo = files.get('passport-photo'),           # file field
            coppy_of_all_degrees = files.get('coppy-of-degrees'),   # file field
            coppy_of_qualifications = files.get('coppy-of-qualifications'),  # file field
            coppy_of_transcripts = files.get('coppy-of-transcripts'),  # file field 
            copies_of_diplomas = files.get('copies-of-diplomas'),   # file field
            nationality = post.get('country')
        )

        messages.success(request, "Your online application was submitted successfully")
        return redirect('userauth:profile')

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
        student = TblStudentsAdmissions.objects.get(email=request.user.email)
        if student:
            form = StudentCreationForm()

            context = {
                'student': student,
                'form': form
            }

            return render(request,template,context)
    except Exception as e:
         messages.error(request, "Requested student record does not exist.Please apply here")
         return redirect('student:online-application')


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

# def upload_course_code_csv(request):
#     if request.method == 'POST':
#         csv_file = request.FILES.get('csv_file')
        
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request, "Please upload a valid CSV file.")
#             return redirect('student:fetch-student-results')

#         # Process the CSV file here
#         # For example, you can read the file and save the course codes to the database

#         messages.success(request, "CSV file uploaded successfully.")
#         return redirect('student:fetch-student-results')
    
#     return render(request, 'student/upload_course_code_csv.html')