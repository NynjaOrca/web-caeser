from flask import Flask, request, redirect, render_template
from caeser import rotate_string
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST'])
def encrypt():
    
#ROT VALUE HANDLING
    rot_value = request.form['rot']
    try:
        rot_value = int(rot_value)
    except ValueError:
        return render_template('value_error_template.html', invalid_char="'" + rot_value + "'")



#MESSAGE HANDLING
    user_message = request.form['text']
    encrypted_message = rotate_string(user_message, rot_value)
    return render_template('caeser_form.html', success_banner="YOUR ENCRYPTED MESSAGE:",message=encrypted_message) 



@app.route("/")
def index():
    return render_template('caeser_form.html', message='')


app.run()