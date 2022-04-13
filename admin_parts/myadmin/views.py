from django.shortcuts import render
from .models import Element
from myadmin.selenium_parts.BaseClass import ElementFinder
from django.http import HttpResponse
from myadmin.selenium_parts.compare_screenshot import compare_screenshot
import os
from myadmin.selenium_parts.BaseClass import BaseClass

from typing import NamedTuple
from selenium.common.exceptions import InvalidArgumentException, InvalidSelectorException


def make_screenshot(Elements: NamedTuple , save_path: str) -> None:
    non_correct_list = []
    for i in Elements:
        url = i.page.page_url
        selector_type = i.selector_type
        selector_text = i.selector_text
        selector_id =i.id
        new_page = ElementFinder(url, selector_type)

        try:
            new_page.go_to_site()
        except InvalidArgumentException:
            return True

        try:
            element = new_page.find_element((new_page.selector_type, selector_text))
        except InvalidSelectorException:
            pass

        element.screenshot(f'{save_path}{selector_id}.png')


def save(request):
    Elements = Element.objects.all()
    isValid = make_screenshot(Elements, './stable_images/' )
    if isValid:
        return HttpResponse("Can't create page object")
    return HttpResponse('all screenhots created')


def compare_image(request):
    Elements = Element.objects.all()
    isValid = make_screenshot(Elements, './today_images/')
    if isValid:
        return HttpResponse("Can't create page object")
    file_list_today = os.listdir('./today_images')
    file_list_stable = os.listdir('./stable_images')
    for fileneme in file_list_today:
        if fileneme in file_list_stable:
             compare_screenshot(f'./today_images/{fileneme}', f'./stable_images/{fileneme}')
    return HttpResponse('all screenhots compared')











    

