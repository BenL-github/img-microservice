import requests
import base64
from PIL import Image
from io import BytesIO

# open file
with open("dog.jpeg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read())

# convert black and white 
r = requests.post("http://127.0.0.1:5000/bwconv", data={"image":encoded_image})

with Image.open(BytesIO(base64.b64decode(r.json()["image"]))) as bw_image:
    bw_image.save("blackandwhite.jpeg", format="JPEG")

# resize file to 50x50 pixels 
r = requests.post(
    "http://127.0.0.1:5000/resize", 
    data={
        "image":encoded_image,
        "width": 50,
        "height": 50
        })

with Image.open(BytesIO(base64.b64decode(r.json()["image"]))) as resized_im:
    resized_im.save("resized.jpeg", format="JPEG")
