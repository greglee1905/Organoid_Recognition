from PIL import Image
import os


#This script  collects all the images, sizes them down to 256 by 256 and renames them!

path = "/Users/greglee/Data_Science/Organoids/Raw_Images/"
path1 = "/Users/greglee/Data_Science/Organoids/Images/"
os.getcwd()

for i,filename in enumerate (os.listdir(path)):
    try:
        #os.rename(path + "/" + filename, path1 + "/" + str(i) + ".jpg")
        sample_image = Image.open(path + "/" + str(i) + ".jpg")
        sample_image = sample_image.resize((256, 256), Image.ANTIALIAS)
        sample_image.save(path1+ "/" + str(i) + "_resize.jpg", quality=100)
    except:
        print("Something went wrong")



