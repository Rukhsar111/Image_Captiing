from Main import Predictor
import json
from flask import Flask, render_template, request, Response, jsonify
import os
from flask_cors import CORS, cross_origin
from utils_2 import decodeImage

app = Flask(__name__)



RENDER_FACTOR = 35

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "file.jpg"
        self.obj_detect= Predictor()


    # def run_inference(img_path='file.jpg'):
    #     # run inference 
    #     result_img = detector.predict(img_path)

    #     # clean up
    #     try:
    #         os.remove(img_path)
    #     except:
    #         pass

    #     return result_img


@app.route("/")
def home():
    # return "Landing Page"
    return render_template("index_2.html")


@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.obj_detect.predict('file.jpg' , task="image_captioning" , question=None, caption=None)

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"
    # return jsonify({"result":result})
    return result


# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    port = 9000
    app.run(host='127.0.0.1', port=port)
