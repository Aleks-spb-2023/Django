import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)
# Create your views here.


def get_about(request):
    logger.info('Info about Eroor !!!!!!!!!!!')

    html = f"<h1>My name is Aleks</h1>" \
           f"<h2>this is my first page</h2>" \
           f"Круто поехали дальше"

    return HttpResponse(html)


def get_home(request):
    logger.info('Info about Eroor !!!!!!!!!!!')
    html = f'<h1 align="center">Главная страница<br> O Себе</h1>' \
           f'<h2>Menu</h2>'\
            f'<h3> nunber menu</h3>'


    return HttpResponse(html)