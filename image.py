import io
import base64
from flask import Flask, request
from PIL import Image

app = Flask(__name__)

@app.route("/")
def home():
    return {"foo":"bar"}

@app.route("/resize", methods=["POST"])
def resize():
    try:
        width = int(request.form["width"])
        height = int(request.form["height"])
        decoded_im = base64.b64decode(request.form["image"])
        resized_im = Image.open(io.BytesIO(decoded_im))

        # resize 
        resized_im = resized_im.resize((width,height))

        # retrieve bytes from Image object and encode it
        result = io.BytesIO()
        resized_im.save(result, format="JPEG")
        result = result.getvalue()
        result = base64.b64encode(result)

        # close image 
        resized_im.close()
        status = 200
        return {"image": result.decode('utf-8')}, status
    except Exception as e:
        result = f"Error: {e}"
        return {"ERROR": result}, 400

@app.route("/bwconv", methods=["POST"])
def bwconv():
    try:
        # receive b64 encoded image data 
        decoded_im = base64.b64decode(request.form["image"])
        bw_image = Image.open(io.BytesIO(decoded_im))
        # convert to black and white
        bw_image = bw_image.convert("L")
        
        # retrieve bytes from Image object and encode it
        result = io.BytesIO()
        bw_image.save(result, format="JPEG")
        result = result.getvalue()
        result = base64.b64encode(result)
        
        # close image
        bw_image.close()
        return {"image": result.decode('utf-8')}, 200
    except Exception as e:
        result = f"Error: {e}"
        return {"ERROR": result}, 400

if __name__ == "__main__":
    app.run()