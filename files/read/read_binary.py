from PIL import Image 
import urllib.request

urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

img = Image.open('dog.jpg')
img.show()
img.display()
