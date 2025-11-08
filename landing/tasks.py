from celery import shared_task
from .models import PhoneSubmission
from pymongo import MongoClient
from django.conf import settings

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def process_phone_submission(phone, ip, user_agent):
    # ذخیره شماره در PostgreSQL
    record = PhoneSubmission.objects.create(
        phone=phone,
        ip=ip,
        user_agent=user_agent,
        processed=True
    )

    # ذخیره لاگ در MongoDB
    client = MongoClient(settings.MONGO_URI)
    db = client["landing_logs"]
    db.submissions.insert_one({
        "phone": phone,
        "ip": ip,
        "user_agent": user_agent,
        "timestamp": record.created_at.isoformat()
    })
    client.close()
