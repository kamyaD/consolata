from django.contrib import admin
from .models import TimetableEntry

# Register your models here.
@admin.register(TimetableEntry)
class TimetableEntryAdmin(admin.ModelAdmin):
    list_display = ['day', 'class_level', 'course_code_first','course_title_first', 'lecturer_first','first_room','course_code_second','course_title_second', 'lecturer_second','second_room','after_break_course_code_first','after_break_course_title_first','after_break_lecturer_first','after_break_first_room','after_break_course_code_second','after_break_course_title_second','after_break_lecturer_second','after_break_second_room',
                    'after_lunch_course_code_first','after_lunch_course_title_first','after_lunch_lecturer_first','lecturer']
    list_filter = ['day', 'class_level', 'lecturer',]