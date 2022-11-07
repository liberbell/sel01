from PIL import Image

img = Image.open("aircraft.jpg")
# img.show()

img = img.resize(1024, 768)
img.show()
img.size