from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.models import TblStudentsAdmissions
from .forms import StudentCreationForm
from django.core.mail import send_mass_mail
from django.db.models import Q
from django.core.mail import EmailMessage


# Create your views here.
@login_required
def view_admin_panel(request):
    template = 'admin/admin_panel.html'
    students = TblStudentsAdmissions.objects.filter(registration_number__isnull=False)


    form = StudentCreationForm()

    context = {
        'students': students,
        'form': form
    }

    return render(request,template,context)

@login_required
def admit_new_student(request):
    if request.method == 'POST':
        post = request.POST
        student = TblStudentsAdmissions.objects.create(
            image= request.FILES.get('photo'),
            registration_number = post.get('reg-no'),
            first_name = post.get('first-name'),
            last_name = post.get('last-name'),
            nationality = post.get('nationality'),
            id_passport = post.get('id-passport'),
            date_of_birth = post.get('birth-date'),
            contact = post.get('contact'),
            email = post.get('email'),
            occupation = post.get('occupation'),
            address = post.get('address'),
            sponsor = post.get('sponsor'),
            admission_year = post.get('year-of-admission'),
            month = post.get('month-of-admission'),
            responsible = post.get('responsible-name'),
            telephone = post.get('telephone'),
            type_of_sponsorship = post.get('type_of_sponsorship'),
            language_spoken = post.get('spoken-language'),
            language_to_learn = post.get('language-to-learn'),
            course_type = post.get('type-of-course'),
            duration = post.get('duration'),
            start_date = post.get('biggining-date'),
            other_courses = post.get('other-courses'),
            # self = post.get('self'),
            modality= post.get('modality_of_study')

        )

        messages.success(request, "Student record created successfully")
        return redirect('consolata_admin:admin-panel')



@login_required
def view_individual_sudent(request, id):
    template = 'admin/individual_stident.html'
    student = TblStudentsAdmissions.objects.get(studentid=id)
    form = StudentCreationForm()

    context = {
        'student': student,
        'form': form
    }

    return render(request,template,context)

@login_required
def view_individual_applicant(request, id):
    template = 'admin/individual_applicant.html'
    student = TblStudentsAdmissions.objects.get(studentid=id)
    form = StudentCreationForm()

    context = {
        'student': student,
        'form': form
    }

    return render(request,template,context)

@login_required
def update_student_records(request, id):
    student = get_object_or_404(TblStudentsAdmissions, studentid=id)

    if request.method == 'POST':
        form = StudentCreationForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student record updated successfully")
            return redirect('consolata_admin:student-panel', id=student.studentid)
        else:
            messages.error(request, "There were errors in the form. Please check and try again.")
    else:
        # This ensures the form is prefilled with student info
        form = StudentCreationForm(instance=student)

    return render(request, 'admin/individual_stident.html', {
        'form': form,
        'student': student
    })

@login_required
def get_mailing_list(request):
    template = 'admin/mailing_list.html'
    students = TblStudentsAdmissions.objects.all()
    for student in students:
        student.name = f"{student.first_name} {student.last_name}"

    context = {
        'students': students,
    }

    return render(request,template,context)

@login_required
def send_bulk_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = 'you@example.com'  # or settings.DEFAULT_FROM_EMAIL

        students = TblStudentsAdmissions.objects.exclude(email__isnull=True).exclude(email__exact='').exclude(mail_status='inactive')

        # Prepare the message tuples
        recipient_messages = [
            (subject, message, from_email, [student.email])
            for student in students
        ]

        send_mass_mail(recipient_messages, fail_silently=False)
        messages.success(request, "Bulk emails sent successfully.")
        return redirect('consolata_admin:mailing-list')  # Replace with your actual redirect

    return render(request, 'admin/mailing_list.html')

@login_required
def send_email_to_ndividual_applicant(request, id):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        attachment = request.FILES.get('attachment')
        from_email = 'you@example.com'  # or settings.DEFAULT_FROM_EMAIL

        student = TblStudentsAdmissions.objects.get(pk=id)

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[student.email]
        )

        if attachment:
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        email.send(fail_silently=False)
        messages.success(request, "Email sent successfully.")
        return redirect('consolata_admin:individual-application', id=id)

    return render(request, 'admin/individual_application.html')

@login_required
def applications(request):
    template = 'admin/applications.html'
    students = TblStudentsAdmissions.objects.filter(registration_number=None)

    

    form = StudentCreationForm()

    context = {
        'students': students,
        'form': form
    }

    return render(request,template,context)