from django.shortcuts import render
from .models import Page
from myadmin.selenium_parts.BaseClass import BaseClass
from django.http import HttpResponse
import sys

def index(request):
    url = Page.objects.all()[0]
    new_page = BaseClass(url, './chromedriver')
    new_page.go_to_site()

    

