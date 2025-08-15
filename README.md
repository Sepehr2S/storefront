
# Storefront API

یک پروژه فروشگاه اینترنتی ساده پیاده‌سازی شده با **Django Rest Framework** که تمرکز اصلی آن روی یادگیری و پیاده‌سازی مفاهیم API، مدیریت احراز هویت با JWT، و بهینه‌سازی Queryها با استفاده از **Django ORM** است.

---

## ✨ ویژگی‌ها

- پیاده‌سازی API با **Django Rest Framework**
- احراز هویت با **JWT** (بوسیله‌ی [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/))
- مدیریت کاربران و ثبت‌نام/ورود با [Djoser](https://djoser.readthedocs.io/)
- استفاده از **Celery + Redis** برای کارهای پس‌زمینه (Background Tasks)
- طراحی Queryها برای کم کردن فشار بر دیتابیس و جلوگیری از دریافت اطلاعات اضافی
- Dockerfile برای اجرای پروژه در محیط ایزوله
- ساختار کد تمیز و قابل توسعه

---

## 🛠 تکنولوژی‌ها

- **Python 3.x**
- **Django 5.x**
- **Django Rest Framework**
- **SimpleJWT**
- **Djoser**
- **Celery**
- **Redis**
- **Docker**
- **MySQL**

---

## 🚀 اجرای پروژه

### 1. اجرای بدون Docker

```bash
# کلون کردن ریپازیتوری
git clone https://github.com/Sepehr2S/storefront.git
cd storefront

# ایجاد و فعال‌سازی محیط مجازی
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# مهاجرت دیتابیس
python manage.py migrate

# اجرای سرور توسعه
python manage.py runserver
