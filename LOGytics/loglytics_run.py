"""
Created on Sat Jul  7 21:24:08 2018

@author : Ruthvic
"""
# https://gogul09.github.io/software/flower-recognition-deep-learning

from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
import os
from werkzeug import secure_filename

# from markupsafe import Markup
# from pymongo import MongoClient  # Database connector
# from bson.objectid import ObjectId  # For ObjectId to work
# from keras.models import load_model
# from keras.preprocessing import image
# from keras.layers import Dense, Activation, Flatten
# import numpy as np
# from keras.applications.resnet50 import ResNet50
# from keras.applications.resnet50 import preprocess_input, decode_predictions

# client = MongoClient('mongodb://ruthvic:ruthvic@ds115569.mlab.com:15569/db1ase')
# db = client.db1ase
# collection = db.ruth_modelkb

app = Flask(__name__)
title = "LOGytics"


# modify=ObjectId()
def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', t=title)


UPLOAD_FOLDER = '/Users/charankottapalli/Desktop/LOGytics/upload/'
ALLOWED_EXTENSIONS = set(['txt', 'png'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/uploader", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.form['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', t=title)
        else:
            return render_template('index.html', t=title)
    return ""


if __name__ == "__main__":
    app.run(debug=True)
