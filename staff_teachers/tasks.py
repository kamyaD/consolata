# userauth/tasks.py

import time
from django_rq import job
from django.core.mail import EmailMessage
from .models import PsychologyRegistration

@job
def send_bulk_email_task(subject, message, from_email, attachment_data=None):
    students = PsychologyRegistration.objects.exclude(email__isnull=True).exclude(email__exact='')
    sent_count = 0
    batch_size = 50

    for i in range(0, len(students), batch_size):
        batch = students[i:i + batch_size]
        for student in batch:
            try:
                email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=from_email,
                    to=[student.email],
                )

                if attachment_data:
                    name, content, content_type = attachment_data
                    email.attach(name, content, content_type)

                email.send(fail_silently=False)
                sent_count += 1
                time.sleep(1.5)  # 1.5s delay between emails
            except Exception as e:
                print(f"Error sending to {student.email}: {e}")

        print(f"Batch {i // batch_size + 1} sent. Pausing before next batch...")
        time.sleep(60)  # pause 1 minute between batches

    print(f"Total emails sent: {sent_count}")
    return sent_count
