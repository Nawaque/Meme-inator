from PIL import Image, ImageDraw, ImageFont
 
# gfg_logo.jpeg image opened using
# open function and assigned to variable named img
img = Image.open('./TEMPLATE/bob.png')
 
# Image is converted into editable form using
# Draw function and assigned to d1
d1 = ImageDraw.Draw(img)
 
# Font selection from the downloaded file
myFont = ImageFont.truetype('./FONTS/IMPACT/Impact.ttf', 20)
 
# Decide the text location, color and font
d1.text((65, 170), "Sample text", fill =(255, 0, 0),font=myFont)
 
# show and save the image
img.show()
img.save("results.jpeg")