import time
import logging
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

logger = logging.getLogger('landing.requests')

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # ذخیره زمان شروع
        request._start_time = time.time()

    def process_response(self, request, response):
        try:
            latency = time.time() - getattr(request, '_start_time', time.time())
            payload = {
                "path": request.path,
                "method": request.method,
                "status": response.status_code,
                "latency": round(latency, 4),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }

            # فقط در حالت DEBUG، اطلاعات IP و User-Agent رو لاگ کن
            if settings.DEBUG:
                payload["ip"] = request.META.get("REMOTE_ADDR")
                payload["user_agent"] = request.META.get("HTTP_USER_AGENT")

            logger.info(payload)

        except Exception as e:
            logger.error(f"Request logging failed: {e}")

        return response
