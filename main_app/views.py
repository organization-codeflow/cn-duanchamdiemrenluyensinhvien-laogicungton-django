from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Trang chủ đơn giản"""
    return render(request, 'home.html', {'title': 'Django Simple Project'})


def about(request):
    """Trang giới thiệu"""
    return HttpResponse("<h1>Về chúng tôi</h1><p>Đây là một dự án Django đơn giản.</p>")
