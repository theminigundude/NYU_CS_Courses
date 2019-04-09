from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import bs4
import sys
import requests

CLASSES = []
Cnumber = ""
Ctopic = ""

# functions
def remove_whitespace(input):
    input = input.replace("\n", "")
    input = input.replace(" ", "")
    return input

def Cnumber_func(input):
    input = remove_whitespace(input)
    input = input.replace(u"\u200b", "")
    return input

def Ctopic_func(input):
    input = remove_whitespace(input)
    input = input.replace("*", "")
    input = input.replace(u"\u00a0", "")
    return input

page = requests.get("https://cs.nyu.edu/dynamic/courses/schedule/?semester=fall_2019")
bsoup = BeautifulSoup(page.content, 'html.parser')
big_div = bsoup.find(class_="schedule-listing")
for small_div in big_div:
    if type(small_div) is not bs4.element.NavigableString:
        Cnumber = list(small_div.children)[1].get_text()
        Ctopic = list(small_div.children)[3].get_text()
        Cnumber = Cnumber_func(Cnumber)
        Ctopic = Ctopic_func(Ctopic)

    new_object = {'class_number': Cnumber, 'class_topic': Ctopic}
    CLASSES.append(new_object);
del CLASSES[0]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


@app.route('/classes', methods=['GET'])
def all_classes():
    return jsonify({
        'status': 'success',
        'classes': CLASSES,
        })


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return ""

if __name__ == '__main__':
    app.run()
