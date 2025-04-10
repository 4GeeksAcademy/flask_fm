import os
from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
ruta_base = os.path.dirname(__file__)  # te da la ruta absoluta del archivo actual
ruta_modelo = os.path.join(ruta_base, "models", "decision_tree_classifier_default_42.sav")
# model = load(open("/workspaces/flask_fm/src/models/decision_tree_classifier_default_42.sav", "rb"))
model = load(open(ruta_modelo, "rb"))
class_dict = {
    "0": "No tiene diabetes",
    "1": "Tiene Diabetes"
}

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])
        val4 = float(request.form["val4"])
        val5 = float(request.form["val5"])
        val6 = float(request.form["val6"])
        val7 = float(request.form["val7"])
        val8 = float(request.form["val8"])
        
        data = [[val1, val2, val3, val4, val5, val6, val7, val8]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)
# https://flask-fm-2.onrender.com/