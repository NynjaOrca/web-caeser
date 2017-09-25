from flask import Flask, request, redirect
from caeser import rotate_string
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST'])
def encrypt():
    
    template = jinja_env.get_template('caeser_form.html')
    value_error_template = jinja_env.get_template('value_error_template.html')



    rot_value = request.form['rot']

    try:
        rot_value = int(rot_value)
    except ValueError:
        return value_error_template.render(invalid_char="'" + cgi.escape(rot_value) + "'")

    user_message = request.form['text']

    encrypted_message = rotate_string(cgi.escape(user_message), rot_value)

    return template.render(success_banner="YOUR ENCRYPTED MESSAGE:",message=encrypted_message) 



@app.route("/")
def index():
    template = jinja_env.get_template('caeser_form.html')
    return template.render(message='')


app.run()