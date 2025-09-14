from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, TblStudentsAdmissions
from django.utils.timezone import now

@receiver(post_save, sender=CustomUser)
def create_student_record(sender, instance, created, **kwargs):
    print("instance===>", instance)
    print("Signal triggered for user:", instance.email)
    if created and instance.role == "Student":
        # Create a TblStudentsAdmissions record when a Student user is created
        TblStudentsAdmissions.objects.create(
            first_name=instance.first_name if hasattr(instance, "first_name") else "",
            last_name=instance.last_name if hasattr(instance, "last_name") else "",
            email=instance.email,
            school=instance.school if hasattr(instance, "school") else "",
            admission_year=str(now().year),  # default to current year
            month=now().strftime("%B"),      # default to current month
        )
