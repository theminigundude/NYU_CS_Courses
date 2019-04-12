from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import bs4
import sys
import requests
import re

CLASSES = []
Cnumber = ""
Ctopic = ""

# functions
def remove_whitespace(input):
    output = re.sub(r'\s+|\t|\n|[*]|[\u200b]', " ", input).strip()
    return output

page = requests.get("https://cs.nyu.edu/dynamic/courses/schedule/?semester=fall_2019")
bsoup = BeautifulSoup(page.content, 'html.parser')
big_div = bsoup.find(class_="schedule-listing")
for small_div in big_div:
    if type(small_div) is not bs4.element.NavigableString:
        #unprocessed info taken through bs4
        course_info_raw = small_div.find_all('span')

        #gets text and strips leading or trailing whitespace
        course_info = list(map(lambda x: remove_whitespace(x.get_text()), course_info_raw))

        new_object = {'class_number': course_info[0],
                'class_topic': course_info[1],
                'professor': course_info[2],
                'time': course_info[3],
                'room': course_info[4]
                }
        CLASSES.append(new_object);

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


@app.route('/')
def root():
    return "root"

if __name__ == '__main__':
    app.run()
