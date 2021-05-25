from PIL import Image 

img = Image.open("sampleImg.jpg")
blackAndWhite = img.convert('L')
blackAndWhite.save("bwsampleImg.jpg")
blackAndWhite.show()