from PIL import Image, ImageDraw, ImageFont
import random
 


for i in range(10):

    # gfg_logo.jpeg image opened using
    # open function and assigned to variable named img
    img = Image.open('./TEMPLATE/bob.png')
    width, height = img.size
    #height = int(height*100/width)
    #width = 100
    #img = img.resize((width, height))

    # Image is converted into editable form using
    # Draw function and assigned to d1
    d1 = ImageDraw.Draw(img)
 
    # Font selection from the downloaded file
    myFont = ImageFont.truetype('./FONTS/IMPACT/Impact.ttf', 40)
 
    for h in range(4):
        #Genère un texte aléatoire
        txt = ""
        for j in range(random.randint(1, 40)):
            txt = txt+chr(random.randint(32, 126))

        # Decide the text location, color and font
        d1.text((random.randint(0, width-len(txt*20)), random.randint(0, height-40)), txt, fill =(255, 255, 255),font=myFont)

    # show and save the image
    # img.show()
    
    img.save("./RESULTS/E_results{}.png".format(i))
    
    
    
    
   
