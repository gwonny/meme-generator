import cv2
import numpy
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

def add_text(img, msg, fontsize, filename, color="white"):
    im = Image.open(img)
    W, H = im.size
    
    if W > 512:
        W = 512
    if H > 512:
        H = 512 
    im = im.resize((W,H))

    top = ''
    bottom = ''

    if "|" in msg:
        top, bottom = msg.split('|')
        draw = ImageDraw.Draw(im)
        style = ImageFont.truetype("impact.ttf", fontsize)
        w1, h1 = style.getsize(top)
        w2, h2 = style.getsize(bottom)
        draw.text(((W-w1)/2,((H-h1)/2)*0.05), top, font=style, fill=color)
        draw.text(((W-w2)/2, ((H-h2))*0.95), bottom, font=style, fill=color)
        im.save(filename)
    else:
        draw = ImageDraw.Draw(im)
        style = ImageFont.truetype("impact.ttf", fontsize)
        w, h = style.getsize(msg)
        if w > W*0.9:
            max_width, _ = style.getsize("a")
            max_size = (W*0.95)/max_width
            print(max_size)
            lines = wrap(msg, int(max_size))
            y_text = ((H-h)/2)*0.05
            for line in lines:
                wrap_width, wrap_height = style.getsize(line)
                draw.text(((W-wrap_width)/2, y_text), line, font=style, fill=color)
                y_text += wrap_height
            im.save(filename)
        else:
            draw.text(((W-w)/2,((H-h)/2)*0.05), msg, font=style, fill=color)
            im.save(filename)
