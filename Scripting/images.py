from PIL import Image, ImageFilter

img = Image.open('./Pokemons/pikachu.jpg')

# gives the format of the image 
print(img.format)

# gives the size of the image in pixels
print(img.size)

# mode is either RGB or CMYK  (Look documentation)
print(img.mode)

# PIL also gives option to filter the image 
filtered_img = img.filter(ImageFilter.SMOOTH)
# saving the filtered image 
filtered_img.save("smooth.png", 'png')

# to convert into black and white, use L. Other format is RGB. 
blw_image = img.convert('L')
blw_image.save("grey.png", 'png')

# to show an image
blw_image.show()

# to rotate an image 
rotated = blw_image.rotate(90)
rotated.show()

# to resize an image
# orignally, pikachu was 640,640. Let's resize to 300,300
resized = img.resize((300,300))
resized.show()

# to resize while preserving the aspect ratio. Works only until (400,400)
img.thumbnail((200,200))
img.show()