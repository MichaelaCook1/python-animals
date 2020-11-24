from flask import Flask,render_template
import requests

app= Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    #gets an animal
    animal = requests.get("localhost:5000/animal")
    #gets the noise
    noise = requests.post("localhost:5001/noise", data=


    return render_template('index.html', animals="", noise="")



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
