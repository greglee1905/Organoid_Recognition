from PIL import Image
import os
import random

#This function goes pulls ten random images from the data set and displays them!

def disp_5_images(path):
    counter = 0
    num_images = len([name for name in os.listdir(path)])
    os.getcwd()

    for images in os.listdir(path):
        counter = counter +1
        image = Image.open(str(path + images))
        assert(image.size[0] ==256 & image.size[1] == 256) #Checking to make sure all the images adhere to the same dimensions

    print(counter)

    for x in range(10):
        rand_numb = random.randint(2, counter)
        print()
        image = Image.open(path + str(rand_numb) + "_resize.jpg")
        image.show()

    return num_images


path = "/Users/greglee/Data_Science/Organoids/Images/"
print(disp_5_images(path))
