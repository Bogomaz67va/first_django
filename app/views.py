from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    msg = f'<p><span style="color: blueviolet;font-weight: bold;">Текущее время</span>: ' \
          f'{current_time}</p><br><a href="{reverse("home")}">на главную</a>'
    return HttpResponse(msg)


def workdir_view(request):
    filename_root_list = list()
    for root, dirs, files in os.walk("./app/"):
        for filename in files:
            filename_root_list.append(f'<li style="max-width: 200px;padding: 5px;'
                                      f'background-color: #79caae;color: ffffff;border: 1px solid #a77676;"'
                                      f'>{filename}</li>')
    str_filename = ','.join(filename_root_list).replace(',', '')
    home_page = f"<br><a href='{reverse('home')}'>на главную</a>"
    return HttpResponse(f"<ul>{str_filename}</ul>{home_page}")
