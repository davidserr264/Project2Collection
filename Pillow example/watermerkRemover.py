import os
import glob
from PIL import Image

currentdir=os.getcwd() #gets the current directory
checker = os.path.exists(currentdir+'/croppedimages')

if checker==False: #checks if folder that holds final results exists, creates if doesnt exsist 
	os.mkdir(currentdir+'/croppedimages')

os.chdir(currentdir+'/imagestocrop/')

images = glob.glob('*.jpg') #creates lsit of files to work on
for image in images:
	if os.path.isfile(currentdir+"/croppedimages/"+image): #if images already cropped, move onto next image
		continue
	else: #crops bottom of image
		img = Image.open(image)
		width, height = img.size
		bottom = height-20
		cropped = img.crop((0, 0, width, bottom))
		cropped.save(currentdir+"/croppedimages/"+image)