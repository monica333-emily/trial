from PIL import Image
image = Image.open("example.jpg")
image.save("example.png", "PNG")
from PIL import Image
image = Image.open("example.png")
new_size = (350,530)
resized_image = image.resize(new_size)
resized_image.show()