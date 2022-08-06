from turtle import width
from wsgiref.util import request_uri
from flask import Flask,jsonify,request,render_template

from project_app.utils import FishWeight

import config

app = Flask(__name__)

@app.route('/')
def hello_flask():

    return "Hello flask"

print("*"*50)

@app.route('/fishweight')
def get_predicted_weight():

    data = request.form

    print("*"*50)

    Length1 = eval(data['Length1'])
    Length2 = eval(data['Length2'])
    Length3 = eval(data['Length3'])
    Height = eval(data['Height'])
    Width = eval(data['Width'])
    Species = (data['Species'])

    weight_obj =FishWeight(Length1, Length2, Length3, Height, Width, Species)

    weight = weight_obj.get_fish_weight()

    return jsonify({'result': f'The predicted weight of fish is {weight}'})

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=config.PORT_NUMBER)