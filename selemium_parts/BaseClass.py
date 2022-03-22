import os
import time

from PIL import Image, ImageChops, ImageDraw
from selenium import webdriver

# driver = webdriver.Chrome('chromedriver')
# # class FindImage:

# driver.get('https://google.com')

# field = driver.find_element_by_xpath('//div[text() = "Россия"]')
# time.sleep(160)
# img1 = field.screenshot('screenshot1.png')



def find_simple_image(img1:str, img2:str, name:str) -> bool:
    image_1 = Image.open(img1).convert('RGB')
    image_2 = Image.open(img2).convert('RGB')
    result = ImageChops.difference(image_1, image_2)
    if image_1.size != image_2.size:
        return False
    box = result.getbbox()

    if box:
        draw1 = ImageDraw.Draw(image_1)
        draw2 = ImageDraw.Draw(image_2)
        draw1.rectangle(result.getbbox(), fill=None, outline=(139,0,0), width = 3)
        draw2.rectangle(result.getbbox(), fill=None, outline=(139,0,0), width = 3)
        image_1.save(f'{name}1.png')
        image_2.save(f'{name}2.png')
    else:
        return False


find_simple_image('screenshot.png', 'screenshot2.png', 'draw')

