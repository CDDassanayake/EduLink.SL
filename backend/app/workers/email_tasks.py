from app.workers.celery_app import celery_app


@celery_app.task
def send_verification_email(email: str, verification_url: str):
    """
    Send email verification email via Resend API.
    """
    # TODO: Implement email sending with Resend API
    pass


@celery_app.task
def send_booking_confirmation_email(student_email: str, booking_details: dict):
    """
    Send booking confirmation email to student.
    """
    # TODO: Implement booking confirmation email
    pass


@celery_app.task
def send_booking_notification_email(teacher_email: str, booking_details: dict):
    """
    Send new booking notification email to teacher.
    """
    # TODO: Implement booking notification email
    pass


@celery_app.task
def send_booking_reminder_email(user_email: str, booking_details: dict, hours_before: int):
    """
    Send booking reminder email (24h and 1h before session).
    """
    # TODO: Implement booking reminder email
    pass


@celery_app.task
def send_verification_approval_email(teacher_email: str):
    """
    Send verification approval email to teacher.
    """
    # TODO: Implement verification approval email
    pass


@celery_app.task
def send_verification_rejection_email(teacher_email: str, reason: str):
    """
    Send verification rejection email to teacher.
    """
    # TODO: Implement verification rejection email
    pass
