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
    
    draw = ImageDraw.Draw(im)
    style = ImageFont.truetype("impact.ttf", fontsize)
    w, h = style.getsize(msg)
    draw.text(((W-w)/2,((H-h)/2)/10), msg, font=style, fill="white")

    im.save(filename)

def main():
    add_text('dababy.jpg', '8===D', 50, 'meme.png')

if __name__ == '__main__':
    main()