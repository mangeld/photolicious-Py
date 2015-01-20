from __future__ import print_function
from PIL import Image, ImageFilter, ImageEnhance

im = Image.open('JPEG/Fraag 4_def_v.2.jpg')
#print(im.format, im.size, im.mode)

width = im.size[0]
height = im.size[1]

if width < height:
	newWidth   = height
	newHeight  = ( newWidth * newWidth ) / width
	blurredImg = im.resize( (newWidth, newHeight), Image.BICUBIC )
	blurredImg = blurredImg.filter( ImageFilter.GaussianBlur( 25 ) )
	blurredImg = blurredImg.crop( (0, (newHeight - height) / 2 , height, height + ((newHeight - height)/2)) )
	enhancer = ImageEnhance.Brightness( blurredImg )
	enhancer = enhancer.enhance(0.86)
	enhancer.paste( im, ( (newWidth - width) / 2 , 0) )
	enhancer.save( 'test.jpg', quality=95 )



