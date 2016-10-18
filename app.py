from flask import *
from os import *
from mongoengine import *
from werkzeug.utils import secure_filename
from bs4 import *
from urllib.request import *

# APP_ROOT = path.dirname(path.abspath(__file__))
# UPLOAD_FILE = path.join(APP_ROOT, "static/film")
#
app = Flask(__name__)
# app.config["UPLOAD_FILE"] = UPLOAD_FILE
# app.config["SECRET_KEY"] = "Ahihi do's ngok's ^-^"
#
# # mongodb://<dbuser>:<dbpassword>@ds053126.mlab.com:53126/hoang
#
# db_name = "hoang"
# host = "ds053126.mlab.com"
# port = 53126
# user_name = "hoang"
# password = "0986369617"
#
# connect(db_name,
#         host=host,
#         port=port,
#         username = user_name,
#         password = password)
#
# class Movie(Document):
#     Title = StringField()
#     Desc = StringField()
#     Image_link = StringField()
#     Rate = FloatField()


@app.route('/')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
