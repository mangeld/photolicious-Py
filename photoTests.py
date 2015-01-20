from __future__ import print_function
from PIL import Image, ImageFilter, ImageEnhance

im = Image.open('JPEG/porsche.jpg')
#print(im.format, im.size, im.mode)

def makeBlurredSquare( im, destination, blur=25, quality=95, blurDarkness=0.86 ):
	width = im.size[0]
	height = im.size[1]

	if width < height:
		newWidth   = height
		newHeight  = ( newWidth * newWidth ) / width
		#Resize so the short side == the initial long side & apply blur
		blurredImg = im.resize( (newWidth, newHeight), Image.BICUBIC ).filter( ImageFilter.GaussianBlur( blur ) )
		#Crop the background to be 1:1
		blurredImg = blurredImg.crop( (0, (newHeight - height) / 2 , height, height + ((newHeight - height)/2)) )
		#Make it darker so it doesn't draw attention
		blurredImg = ImageEnhance.Brightness( blurredImg ).enhance( blurDarkness )
		#Paste the original image in the center
		blurredImg.paste( im, ( (newWidth - width)/2 , 0) )
		blurredImg.save( destination, quality=quality )
	else:
		newWidth   = ( width * width ) / height
		newHeight  = width
		blurredImg = im.resize( ( newWidth, newHeight ), Image.BICUBIC ).filter( ImageFilter.GaussianBlur( blur ) )
		blurredImg = blurredImg.crop( ( (newWidth - newHeight)/2 , 0, newWidth - ((newWidth - newHeight)/2) ,newHeight ) )
		blurredImg = ImageEnhance.Brightness( blurredImg ).enhance( blurDarkness )
		blurredImg.paste( im, ( 0, (newHeight-height)/2) )
		blurredImg.save( destination, quality=quality )