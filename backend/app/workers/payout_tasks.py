from app.workers.celery_app import celery_app


@celery_app.task
def process_weekly_payouts():
    """
    Process weekly payouts to teachers via Stripe Connect.
    This should run every week via Celery beat.
    """
    # TODO: Implement weekly payout processing
    pass


@celery_app.task
def queue_teacher_payout(teacher_id: str, booking_id: str, amount: float):
    """
    Queue a payout for a teacher after a session is attended.
    """
    # TODO: Implement individual payout queuing
    pass
