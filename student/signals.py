from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, TblStudentsAdmissions
from django.utils.timezone import now

@receiver(post_save, sender=CustomUser)
def create_student_record(sender, instance, created, **kwargs):
    print("instance===>", instance)
    print("Signal triggered for user:", instance.email)

    if created and instance.role == "Student":
        # Check if a student with this email already exists
        if not TblStudentsAdmissions.objects.filter(email=instance.email).exists():
            TblStudentsAdmissions.objects.create(
                first_name=getattr(instance, "first_name", ""),
                last_name=getattr(instance, "last_name", ""),
                email=instance.email,
                school=getattr(instance, "school", ""),
                admission_year=str(now().year),  # default to current year
                month=now().strftime("%B"),      # default to current month
            )
            print(f"Student record created for {instance.email}")
        else:
            print(f"Student record for {instance.email} already exists. Skipping creation.")
