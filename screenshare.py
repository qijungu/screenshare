# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask.templating import render_template
import json
from screen import screenlive

secret_key = u'f71b10b68b1bc00019cfc50d6ee817e75d5441bd5db0bd83453b398225cede69'

app = Flask(__name__)
app.secret_key = secret_key
Bootstrap(app)

###### general ##########################################
@app.route('/')
def welcome():
    return render_template("screen.html")

@app.route('/screenfeed/', methods=["POST"])
def screenfeed():
    return json.dumps([True, screenlive.gen()])

### main ###
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
