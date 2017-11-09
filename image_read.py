import base64

image = open('terrain_2.jpg','rb')
image_read = image.read()
image_64_encoded = base64.encodestring(image_read)
print(image_64_encoded)
