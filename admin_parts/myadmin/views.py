from django.shortcuts import render
from .models import Element
from myadmin.selenium_parts.BaseClass import ElementFinder
from django.http import HttpResponse
from myadmin.selenium_parts.compare_screenshot import compare_screenshot
import os
from myadmin.selenium_parts.BaseClass import BaseClass
import time
from typing import NamedTuple


def make_screenshot(Elements: NamedTuple , save_path: str) -> None:
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
        element.screenshot(f'{save_path}{selector_id}.png')


def save(request):
    Elements = Element.objects.all()
    make_screenshot(Elements, './stable_images/' )
    return HttpResponse('all screenhots created')


def compare_image(request):
    Elements = Element.objects.all()
    make_screenshot(Elements, './today_images/')
    file_list_today = os.listdir('./today_images')
    file_list_stable = os.listdir('./stable_images')
    for fileneme in file_list_today:
        if fileneme in file_list_stable:
             compare_screenshot(f'./today_images/{fileneme}', f'./stable_images/{fileneme}')
    return HttpResponse('all screenhots compared')











    

