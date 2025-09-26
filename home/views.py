from django.shortcuts import render

from .models import News, Event, Testimonial
from django.contrib.auth.decorators import login_required



# Create your views here.
# def home(request):
#     students = TblStudentsAdmissions.objects.all()
#     print(students.count())

#     return render(request, 'home/index.html', {'students': students.count() })

def psychology_school(request):
    return render(request, 'home/psychology.html')

def theology_school(request):
    return render(request, 'home/theology.html')

def philosophy_school(request):
    return render(request, 'home/philosophy.html')

def language_center(request):
    return render(request, 'home/language.html')

def history(request):
    return render(request, 'home/history.html')

def leadership(request):
    return render(request, 'home/leadership.html')

def requirements(request):
    return render(request, 'home/requirements.html')

def home(request):
    latest_news = News.objects.order_by("-created_at")[:3]
    upcoming_events = Event.objects.order_by("date")[:3]
    testimonials = Testimonial.objects.all()[:3]

    return render(request, "home/index.html", {
        "latest_news": latest_news,
        "upcoming_events": upcoming_events,
        "testimonials": testimonials,
    })

@login_required
def library(request):
    return render(request, 'home/library.html')

@login_required
def e_resources(request):
    return render(request, 'home/e-resources.html')

