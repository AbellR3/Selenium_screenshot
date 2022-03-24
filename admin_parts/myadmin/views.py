from django.shortcuts import render
from .models import Element
from myadmin.selenium_parts.BaseClass import ElementFinder
from django.http import HttpResponse
import sys
from myadmin.selenium_parts.BaseClass import BaseClass
import time
import typing


def save(request):
    Elements = Element.objects.all()
    for i in Elements:
        url = i.page.page_url
        selector_type = i.selector_type
        selector_text = i.selector_text
        selector_id =i.id
        new_page = ElementFinder(url, selector_type)
        #need to add try/except
        new_page.go_to_site()
        #need to add try/except
        element = new_page.find_element((new_page.selector_type, selector_text))
        #need to add try/except
        element.screenshot(f'./stable_images/stableId_{selector_id}.png')

    return HttpResponse('all screenhots created')







    

