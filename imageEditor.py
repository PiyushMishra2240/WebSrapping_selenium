from PIL import Image, ImageEnhance, ImageFilter
import os

path = '../Pics_test'
pathout = '../Pics_test/Edited'


for filename in os.listdir(path):
    # print(filename)
    if filename == 'Edited':
        continue
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'{pathout}/{clean_name}_edited.jpg')