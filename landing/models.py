from django.db import models
from django.utils import timezone

class PhoneSubmission(models.Model):
    phone = models.CharField(max_length=20)
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    processed = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['phone']),
        ]

    def __str__(self):
        return self.phone
