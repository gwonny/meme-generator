import cv2
import numpy
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

def find_color_text(text, prefix, default_color):
    p = len(prefix)
    for i in range(len(text)-p + 1):
        if prefix == text[i:i+p]:
            return text[i+p:].strip()
    return default_color


def place_text(W, w, H, h, style, msg, color, draw, pos):
    if pos == 'top':
        y_init_factor = 0.05
        print_direction = 1
    else:
        y_init_factor = 0.95*2
        print_direction = -1

    if w > W*0.9:
        max_width, _ = style.getsize("a")
        max_size = (W*0.95)/max_width
        lines = wrap(msg, int(max_size))

        # set initial y position 
        _, wrap_height = style.getsize(lines[0])    
        y_text = ((H-h)/2)*y_init_factor
        if pos == 'bot':
            lines.reverse()

        for line in lines:
            wrap_width, wrap_height = style.getsize(line)
            draw.text(((W-wrap_width)/2, y_text), line, font=style, fill=color)
            y_text += (wrap_height*print_direction)
    else:
        draw.text(((W-w)/2,((H-h)/2)*y_init_factor), msg, font=style, fill=color)

def add_text(img, msg, fontsize, filename, top='', bottom='', color='white'):
    top = top.strip()
    bottom = bottom.strip()

    im = Image.open(img)
    W, H = im.size
    
    if W > 512:
        W = 512
    if H > 512:
        H = 512 
    im = im.resize((W,H))

    draw = ImageDraw.Draw(im)
    style = ImageFont.truetype("impact.ttf", fontsize)

    if top and bottom:
        w1, h1 = style.getsize(top)
        w2, h2 = style.getsize(bottom)
        place_text(W, w1, H, h1, style, top, color, draw, 'top')
        place_text(W, w2, H, h2, style, bottom, color, draw, 'bot')
    elif top:
        w, h = style.getsize(top)
        place_text(W, w, H, h, style, top, color, draw, 'top')
    elif bottom:
        w, h = style.getsize(bottom)
        place_text(W, w, H, h, style, bottom, color, draw, 'bot')
    
    im.save(filename)