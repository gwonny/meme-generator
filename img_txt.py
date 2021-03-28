#!/usr/bin/python3
# coding=utf-8
import cv2
import numpy
# from PIL import Image, ImageDraw, ImageFont

'''
def add_text(img, txt, left, top, text_color, size=20):
	if (isinstance(img, numpy.ndarray)):
		img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

		drawer = ImageDraw.Draw(img)

		style = ImageFont.truetype("impact.ttf", size)

		drawer.text((left, top), txt, text_color, font=style)

		return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
'''

def add_text()

def main():
	
	src = cv2.imread('DSC01661.jpg', 1)
	cv2.waitKey(0)
	dim = src.shape
	factor = 0.0
	print(type(dim[0]))
	
	if (dim[0] > dim[1]):
		factor = float(dim[0]) / 500.0
	else:
		factor = float(dim[1]) / 500.0

	text = "WHAT THE FUCK BRO"

	font = cv2.FONT_HERSHEY_SIMPLEX

	textsize = cv2.getTextSize(text, font, 1, 2)[0]

	textX = int((dim[0] - textsize[0]) / 2)
	textY = int((dim[1] - textsize[1]) / 2)

	dim = (int(dim[0] / factor), int(dim[1] / factor))
	src = cv2.resize(src, dim)

	#img = add_text(src, "Hello there", textX, textY, (255,255,255), int(dim[1]*0.2))
	new_img = cv2.putText(src, text, (textX, textY), font, 1, (255,255,255), 2)

	cv2.imshow('text image', new_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
   
	

if __name__ == '__main__':
	main()