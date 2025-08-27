# Django Simple Project

Dự án Django Python đơn giản nhất có thể chạy ngay lập tức.

## Cấu trúc dự án

```
django/
├── manage.py
├── requirements.txt
├── README.md
├── simple_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main_app/
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│   └── urls.py
└── templates/
    ├── base.html
    └── home.html
```

## Cài đặt và chạy

### 1. Tạo virtual environment (khuyến nghị)

```bash
python -m venv venv
```

### 2. Kích hoạt virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 4. Chạy migration (tạo database)

```bash
python manage.py migrate
```

### 5. Tạo superuser (tùy chọn)

```bash
python manage.py createsuperuser
```

### 6. Chạy server

```bash
python manage.py runserver
```

## Truy cập ứng dụng

- **Trang chủ:** http://127.0.0.1:8000/
- **Trang giới thiệu:** http://127.0.0.1:8000/about/
- **Admin:** http://127.0.0.1:8000/admin/ (nếu đã tạo superuser)

## Tính năng có sẵn

- ✅ Cấu hình Django cơ bản
- ✅ Template system với base template
- ✅ URL routing
- ✅ Admin interface
- ✅ SQLite database
- ✅ Static files handling
- ✅ Responsive design cơ bản

## Phát triển tiếp

Dự án này là nền tảng để bạn có thể:

1. Thêm models trong `main_app/models.py`
2. Tạo thêm views và templates
3. Cấu hình static files và media
4. Thêm authentication
5. Tích hợp với database khác
6. Deploy lên production

## Cấu trúc code

- **`simple_django/`**: Cấu hình chính của dự án
- **`main_app/`**: Ứng dụng chính với views và URLs
- **`templates/`**: HTML templates
- **`manage.py`**: Command-line utility của Django

Dự án đã sẵn sàng để bắt đầu phát triển!
