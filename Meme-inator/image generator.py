from PIL import Image, ImageDraw, ImageFont
 
# gfg_logo.jpeg image opened using
# open function and assigned to variable named img
img = Image.open('./TEMPLATE/200x200.png')
 
# Image is converted into editable form using
# Draw function and assigned to d1
d1 = ImageDraw.Draw(img)

#image size
width = img.size[0]
height = img.size[1]
 
# Font selection from the downloaded file
myFont = ImageFont.truetype('./FONTS/IMPACT/Impact.ttf', 7)
 
# Decide the text location, color and font
d1.text((width/3-3, height/2-20), "caractere random", fill =(255, 255, 255),font=myFont)
 
# show and save the image
#img.show()
img.save("./RESULTS/results9.jpeg")