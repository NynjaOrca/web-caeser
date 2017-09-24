from flask import Flask, request
from caeser import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <!-- create your form here -->
            <form action="/" method ="post">
                <label> Rotate by:
                    <input type="text" name="rot"/>
                    <textarea name="text">
                    </textarea>
                </label>
                <input type="submit" value="Submit Query"/>
            </form>
        </body>
    </html>
    """

@app.route('/', methods=['POST'])
def encrypt():
    rot_value = request.form['rot']


    user_message = request.form['text']


@app.route("/")
def index():
    return (form)

app.run()