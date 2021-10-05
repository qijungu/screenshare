#Copyright (C) 2021  Qijun Gu
#
#This file is part of Screenshare.
#
#Screenshare is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Screenshare is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Screenshare. If not, see <https://www.gnu.org/licenses/>.

from flask import Flask, request, flash, session
from flask_bootstrap import Bootstrap
from flask.templating import render_template
import json, argparse
from screen import screenlive
from werkzeug.utils import redirect

secret_key = u'f71b10b68b1bc00019cfc50d6ee817e75d5441bd5db0bd83453b398225cede69'

app = Flask(__name__)
app.secret_key = secret_key
Bootstrap(app)

###### general ##########################################
@app.route('/')
def welcome():
    session.clear()
    if len(screenlive.password) == 0 :
        session['access'] = True
        return render_template("screen.html")
    else :
        return render_template("login.html")

@app.route('/login', methods = ['POST'])
def login():
    # password is not required
    session.clear()
    if len(screenlive.password) == 0 :
        session['access'] = True
        return render_template("screen.html")

    p = request.form["password"]
    if p == screenlive.password :
        session['access'] = True
        return render_template("screen.html")
    else :
        session.clear()
        flash("Wrong password")
        return render_template("login.html")

@app.route('/screenfeed/', methods=["POST"])
def screenfeed():
    if 'access' in session and session['access']:
        return json.dumps([True, screenlive.gen()])
    else:
        redirect('/')

### main ###
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port, default 18331", type=int, default=18331)
    parser.add_argument("-w", "--password", help="password, default no password", default="")
    parser.add_argument("-s", "--https", help="enable https, default http", action="store_true")
    parser.add_argument("-c", "--cert", help="certificate file")
    parser.add_argument("-k", "--key", help="private key file")

    parser.print_help()
    args = parser.parse_args()
    port = args.port
    screenlive.password = args.password
    
    try:
        if args.https:
            if args.cert and args.key:
                app.run(host='0.0.0.0', port=port, threaded=True, ssl_context=(args.cert, args.key))
            else:
                app.run(host='0.0.0.0', port=port, threaded=True, ssl_context='adhoc')
        else:
            app.run(host='0.0.0.0', port=port, threaded=True)
    except Exception as e:
        print(e.message)
        print("Some errors in the command, fall back to the default http screen sharing!!!\n")
        app.run(host='0.0.0.0', port=port, threaded=True)
