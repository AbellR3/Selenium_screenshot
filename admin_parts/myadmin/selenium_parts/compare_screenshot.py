from PIL import Image, ImageChops, ImageDraw
import re

def find_simple_image(img1:str, img2:str, name:str = 'mistake') -> bool:
    image_1 = Image.open(img1).convert('RGB')
    image_2 = Image.open(img2).convert('RGB')
    img1_index =''.join(re.split('\D', img1))
    img2_index =''.join(re.split('\D', img1))
    result = ImageChops.difference(image_1, image_2)
    if image_1.size != image_2.size:
        return False
    box = result.getbbox()

    if box:
        draw1 = ImageDraw.Draw(image_1)
        draw2 = ImageDraw.Draw(image_2)
        draw1.rectangle(result.getbbox(), fill=None, outline=(139,0,0), width = 3)
        draw2.rectangle(result.getbbox(), fill=None, outline=(139,0,0), width = 3)
        image_1.save(f'./reports/{name}{img1_index}.png')
        image_2.save(f'./reports/{name}{img2_index}.png')
    else:
        return False

find_simple_image('stableId_3.png', 'stableId_33.png')
find_simple_image('stableId_4.png', 'stableId_44.png')