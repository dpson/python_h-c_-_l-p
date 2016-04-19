from flask import Flask, render_template , request
from code_cua_thao import *
import smtplib

connect('test',host = "mongodb://c4e3:c4e3@ds023530.mlab.com:23530/restaurant-c4e3")

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def template():
    if request.method == 'POST':


