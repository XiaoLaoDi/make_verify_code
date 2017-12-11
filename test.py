#!/usr/bin/python
# coding: utf-8

import random
import uuid
import os

from PIL import Image, ImageDraw, ImageFont

NUM = [chr(i) for i in range(0x30, 0x39)]
UPPER = [chr(i) for i in range(0x41, 0x5a)]
LOWER = [chr(i) for i in range(0x61, 0x7a)]
LETTER = (NUM + UPPER + LOWER) * 2

PIC_SIZE = 100, 30  # width and high
FONTS = os.listdir('fonts/')

PIC_PATH = 'source_img/'
SUFFIX = '.png'


def get_code_and_position():
    return random.sample(LETTER, 4), sorted(random.sample(range(80), 4))


def get_verify_pic():
    image = Image.new('RGB', PIC_SIZE, BACKGROUND_COLOR)
    font = ImageFont.truetype(FONT, FONT_SIZE)
    draw = ImageDraw.Draw(image)
    code, position = get_code_and_position()
    draw.text((position[0], random.randint(0, 15)), code[0], font=font, fill=FONT_COLOR)
    draw.text((position[1], random.randint(0, 15)), code[1], font=font, fill=FONT_COLOR)
    draw.text((position[2], random.randint(0, 15)), code[2], font=font, fill=FONT_COLOR)
    draw.text((position[3], random.randint(0, 15)), code[3], font=font, fill=FONT_COLOR)
    pic_name = str(uuid.uuid1()) + SUFFIX
    image.save(PIC_PATH + pic_name, 'png')
    # return code, pic_name
    print(code, pic_name)


if __name__ == '__main__':
    for i in range(50):
        BACKGROUND_COLOR = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        FONT_COLOR = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        FONT_SIZE = random.randint(15, 25)
        FONT = 'fonts/' + FONTS[random.randint(0, len(FONTS)-1)]
        get_verify_pic()