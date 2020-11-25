from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/animal', methods=['GET'])
def animals():
    animals = ["Lion", "Dog", "Cat", "Cow", "Pig", "Snake"]
    return Response(random.choices(animals), mimetype="text/plain")

@app.route('/noise', methods=['POST'])
def noise():
    animal = request.data.decode('utf-8')
    if animal == "Lion":
        noise = "ROAR"
    elif animal == "Dog":
        noise = "WOOF"
    elif animal == "Cat":
        noise = "MEOW"  
    elif animal == "Cow":
        noise = "MOO"
    elif animal == "Pig":
        noise = "OINK"
    elif animal == "Snake":
        noise = "HISS"
    return Response(noise, mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
