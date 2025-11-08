from django.contrib import admin

from .models import PhoneSubmission


@admin.register(PhoneSubmission)
class PhoneSubmissionAdmin(admin.ModelAdmin):
    list_display = ("phone", "ip", "user_agent", "created_at", "processed")
    list_filter = ("processed", "created_at")
    search_fields = ("phone", "ip", "user_agent")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("اطلاعات کاربر", {"fields": ("phone", "processed")}),
        ("اطلاعات فنی درخواست", {"fields": ("ip", "user_agent", "created_at")}),
    )

    def has_add_permission(self, request):
        # جلوگیری از اضافه کردن دستی از پنل ادمین
        return False
