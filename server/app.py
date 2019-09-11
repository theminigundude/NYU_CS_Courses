from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import bs4
import sys
import requests
import re
from datetime import datetime, timedelta

CLASSES = []
Cnumber = ""
Ctopic = ""
#Find the start and end date of the week given the current day
today = datetime.today()
start = today - timedelta(days= today.weekday())
end = start + timedelta(days=6)
start_day = start.strftime("%Y-%m-%d %H:%M")
end_day = end.strftime("%Y-%m-%d %H:%M")

# functions
def remove_whitespace(input):
    output = re.sub(r'\s+|\t|\n|[*]|[\u200b]', " ", input).strip()
    return output

#Remove the extra string when scrape
def remove_extra(prof_name):
    if "Office Hours" in prof_name:
        output = prof_name.replace("Office Hours", "").strip()
        return output
    return prof_name

#Remove the extra string in the course title
def remove_extra_courses(course):
    if "(No Prior Experience)" in course:
        output = course.replace("(No Prior Experience)", "").strip()
        return output
    return course

#Remove the section number for storing data
def parse_course(course_number):
    return "-".join(course_number.split("-",2)[:2])

page = requests.get("https://cs.nyu.edu/dynamic/courses/schedule/?semester=fall_2019&level=UA")
bsoup = BeautifulSoup(page.content, 'html.parser')
big_div = bsoup.find(class_="schedule-listing")
#print(big_div)
for small_div in big_div:
    if type(small_div) is not bs4.element.NavigableString:
        #unprocessed info taken through bs4
        course_info_raw = small_div.find_all('span')
        #gets text and strips leading or trailing whitespace
        course_info = list(map(lambda x: remove_whitespace(x.get_text()), course_info_raw))
        #print(len(course_info))
        new_object = {
                # Start and end are tests ONLY. Plz parse
                #add field short title
                'start': start_day,
                'end': end_day,
                'class_number': parse_course(course_info[0]),
                'title': remove_extra_courses(course_info[1]),
                'professor': remove_extra(course_info[2]),
                'time': course_info[3],
                'room': course_info[4],
                'description': course_info[5]
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
