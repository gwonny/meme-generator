import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

def add_text(img, msg, fontsize, filename):
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
        draw.text(((W-w1)/2,((H-h1)/2)/10), top, font=style, fill="white")
        draw.text(((W-w2)/2, ((H-h2))*0.9), bottom, font=style, fill="white")
        im.save(filename)
    else:
        draw = ImageDraw.Draw(im)
        style = ImageFont.truetype("impact.ttf", fontsize)
        w, h = style.getsize(msg)
        draw.text(((W-w)/2,((H-h)/2)/10), msg, font=style, fill="white")
        im.save(filename)

def main():
    add_text('400.jpg', 'hunter x | hunter ', 50, '400.png')

if __name__ == '__main__':
    main()





# 300 x 300 = 11 chars
# 400 x 400 = 18 chars
# 500 x 500 = 23 chars



