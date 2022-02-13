from PIL import Image, ImageDraw, ImageFont
import random, os
import OpenCV
 

for a in range(39):
    print(a)
    for i in range(3):

        #Ouvre le template à utiliser et récupère sa taille
        img1 = Image.open('./TEMPLATE/Tem{}.jpg'.format(a))
        width, height = img1.size

        #Si voulu, le programme peut redimensioner l'image avec une largeur définie
        #larg = 100
        #height = int(height*larg/width)
        #width = larg
        #height = 224
        #width = 224
        #img1 = img1.resize((width, height))

        # On transforme l'image en un format éditable
        d1 = ImageDraw.Draw(img1)

        img2 = Image.new('1', (width, height))
        d2 = ImageDraw.Draw(img2)
 
        # Font selection from the downloaded file
        #myFont = ImageFont.truetype('./FONTS/TEST/Kingthings_Trypewriter_2.ttf', 40)

        #print(".\FONTS\IMPACT"+chr(92)+random.choice(os.listdir(".\FONTS\IMPACT")))
        #myFont = ImageFont.truetype(".\FONTS\TEST"+chr(92)+random.choice(os.listdir(".\FONTS\TEST")), 40)
 
    
        for h in range(4):
            #Genère un texte aléatoire
            txt = ""
            for j in range(random.randint(1, 40)):
                txt = txt+chr(random.randint(32, 126))

            # Decide the text location, color and font
            font = int(width/20)
            myFont = ImageFont.truetype(".\FONTS\TEST"+chr(92)+random.choice(os.listdir(".\FONTS\TEST")), font)

            x = random.randint(0, width-int(len(txt)*font/2))
            y = random.randint(0, height-font)
            d1.text((x, y), txt, fill =(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),font=myFont)
            d2.text((x, y), txt, fill =(1),font=myFont)

        # show and save the image
        # img.show()
    
        img1.save("./RESULTS/E_results{}-{}.jpg".format(a, i))
        img2.save("./MASKS/E_results{}-{}.png".format(a, i))
    
    
    
    
   
