# Image Resizing/Black&White Microservice 

## How to Request Data

To use the service, you must b64 encode the image file that you want to transform. 

To convert the image to **grayscale/black&white**, place the b64 encoded image in the body of a HTTP POST request. The body should be in JSON format, like so:

{ 
    "image": [base64 encoded image] 
}

Example in Python:

```
with open("dog.jpeg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read())

r = requests.post("http://127.0.0.1:5000/bwconv", data={"image":encoded_image})
```

To **resize** the image, place the b64 encoded image in the body of a HTTP POST request. Additionally, included the resize specificiations. The body should be in JSON format, like so:

{ 
    "image": [base64 encoded image],
    "height": [new height in pixels],
    "width": [new width in pixels]
}

Example in Python:

```
r = requests.post(
    "http://127.0.0.1:5000/resize", 
    data={
        "image":encoded_image,
        "width": 50,
        "height": 50
        })
```

## How to Receive Data

After successfuly sending an HTTP POST you will receive a status code of 200 in the HTTP RESPONSE. Failures will indicate a status code of 400.

The body of the HTTP RESPONSE, will have the transformed image. Before saving the image, you must b64 decode the image. 

Example in Python:
```
with Image.open(BytesIO(base64.b64decode(r.json()["image"]))) as resized_im:
    resized_im.save("resized.jpeg", format="JPEG")
```

## UML Diagram

![UML Diagram](/images/CS361%20UML.jpeg)