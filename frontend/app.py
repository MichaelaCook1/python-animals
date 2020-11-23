from flask import Flask,render_template

app= Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    #gets an animal


    #gets the noise


    return render_template('index.html', animals="", noise="")



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
