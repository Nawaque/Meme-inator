from PIL import Image, ImageDraw, ImageFont
import random
import csv

pathTemplates = "./TEMPLATE/"
pathResults = "./RESULTS/"
data=[]
for i in range(10):

    # gfg_logo.jpeg image opened using
    # open function and assigned to variable named img
    pathTemplate = pathTemplates + "bob.png"
    img = Image.open(pathTemplate)
    width, height = img.size
    #height = int(height*100/width)
    #width = 100
    #img = img.resize((width, height))

    # Image is converted into editable form using
    # Draw function and assigned to d1
    d1 = ImageDraw.Draw(img)
 
    # Font selection from the downloaded file
    myFont = ImageFont.truetype('./FONTS/IMPACT/Impact.ttf', 40)
    
    
    filename = "./CSVs/results.csv"
    
    # writing to csv file 
    
    for h in range(4):
        #Genère un texte aléatoire
        txt = ""
        for j in range(random.randint(1, 40)):
            txt = txt+chr(random.randint(32, 126))

        # Decide the text location, color and font
        d1.text((random.randint(0, width-len(txt*20)), random.randint(0, height-40)), txt, fill =(255, 255, 255),font=myFont)
    pathResult = pathResults + "V_results{}.png".format(i)
    img.save(pathResult)
    data.append([pathTemplate, pathResult ])
print(data)
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)        
    # writing the data rows 
    csvwriter.writerow(["meme", "template"])
    csvwriter.writerows(data)
    # show and save the image
    # img.show()
    
    
