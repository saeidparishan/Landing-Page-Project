

[# Landing Page Project<img width="890" height="483" alt="Screenshot from 2025-11-08 20-06-08" src="https://github.com/user-attachments/assets/3510b2ac-b52f-4055-9d76-e6c474f895e7" />


**Landing Page Project** یک پروژه Django برای ثبت شماره موبایل با پاسخ فوری و ذخیره‌سازی آسنکرون است. این پروژه با استفاده از Docker برای توسعه و استقرار آسان آماده شده است.

---

## Features / ویژگی‌ها

- ثبت شماره موبایل با پاسخ فوری
- پردازش آسنکرون با Celery و Redis
- استفاده از PostgreSQL برای دیتابیس اصلی
- ذخیره لاگ‌ها و آنالیز در MongoDB
- مستندسازی API با Swagger و Redoc
- Dockerized برای استقرار سریع

---

## Technologies / تکنولوژی‌ها

- Python 3.12
- Django
- Django REST Framework (DRF)
- Celery
- Redis
- PostgreSQL
- MongoDB
- Docker & Docker Compose
- Swagger / Redoc برای مستندات API

---

## Installation / نصب

1. کلون کردن پروژه:

```bash
git clone https://github.com/yourusername/landing_project.git
cd landing_project
  ```
ایجاد فایل محیطی و ویرایش متغیرها در صورت نیاز:
cp .env.example .env

----
ساخت و اجرای کانتینرهای Docker:
docker compose build
docker compose up

----
Usage / استفاده

API برای ثبت شماره موبایل:

POST api/v1/submit-phone/


مستندات API:

Swagger UI: http://localhost/swagger/

Redoc: http://localhost/redoc/

پنل مدیریت:

URL: http://localhost/admin/

----
Code Quality / کیفیت کد

پروژه از flake8، isort و black برای حفظ کیفیت کد استفاده می‌کند.

اجرای چک‌ها:
flake8
isort --check-only .
black --check .

----
Environment Variables / متغیرهای محیطی
Variable	Description
DJANGO_DEBUG	True برای توسعه، False برای پروداکشن
POSTGRES_DB	نام دیتابیس PostgreSQL
POSTGRES_USER	نام کاربری PostgreSQL
POSTGRES_PASSWORD	پسورد PostgreSQL
POSTGRES_HOST	هاست PostgreSQL (db برای Docker)
REDIS_URL	URL Redis برای Celery
MONGO_URI	URI MongoDB برای ذخیره لاگ‌ها
DJANGO_SETTINGS_MODULE	ماژول تنظیمات Django (core.settings.development یا core.settings.production)

----
Docker / داکر

سرویس‌ها در Docker Compose تعریف شده‌اند:

web: اجرای Django با Gunicorn

celery: پردازش آسنکرون

db: PostgreSQL

redis: Redis

mongo: MongoDB

nginx: سرور معکوس

برای راه‌اندازی همه سرویس‌ها:

docker compose up

-----
](https://github.com/saeidparishan/Landing-Page-Project/new/main?filename=README.md)
