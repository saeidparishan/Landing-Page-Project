from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

from .serialziers import PhoneSerializer
from landing.tasks import process_phone_submission

@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class SubmitPhoneAPIView(APIView):
    """
    ثبت شماره موبایل با پاسخ فوری و ذخیره‌سازی آسنکرون
    """

    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data['phone']
        ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        # ارسال به صف celery
        process_phone_submission.delay(phone, ip, user_agent)

        return Response(
            {"detail": "شماره شما با موفقیت ثبت شد"},
            status=status.HTTP_202_ACCEPTED
        )
