from requests import get
from bs4 import BeautifulSoup

url = 'https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/registration/classroom-locations.html'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
tl_container = html_soup.find_all('td', class_ = 'table-no-sort-td TL TL')
td_container = html_soup.find_all('td', class_ = 'table-no-sort-td TD TL')
dict = {}
total_list = tl_container + td_container
dict = {}
for i in range(0, len(total_list), 2):
    building_code = total_list[i].text.replace('\n', '').replace('\t','')
    building_real = total_list[i + 1].text.replace('\n', '').replace('\t','')
    dict.update({building_code : building_real})