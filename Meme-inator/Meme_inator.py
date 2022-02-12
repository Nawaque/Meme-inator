from PIL import Image, ImageDraw, ImageFont
import random, os
 

for a in range(27):
    
    for i in range(20):

        #Ouvre le template à utiliser et récupère sa taille
        img1 = Image.open('./TEMPLATE/Tem{}.jpg'.format(a))
        width, height = img1.size

        #Si voulu, le programme peut redimensioner l'image avec une largeur définie
        #larg = 100
        #height = int(height*larg/width)
        #width = larg
        #img = img.resize((width, height))
        img = img.resize((224, 224))

        # On transforme l'image en un format éditable
        d1 = ImageDraw.Draw(img1)

        #img2 = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        img2 = Image.new('RGBA', (224, 224), (0, 0, 0, 0))
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
            d2.text((x, y), txt, fill =(255, 255, 255),font=myFont)

        # show and save the image
        # img.show()
    
        img1.save("./RESULTS/E_results{}-{}.jpg".format(a, i))
        img2.save("./MASKS/E_results{}-{}.png".format(a, i))

    
    
    
    
    
   
