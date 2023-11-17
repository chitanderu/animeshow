
import requests
from bs4 import BeautifulSoup
import csv
def extract_person_info(person_div):
    href = person_div.find('a', target='_blank')['href']
    img_src = person_div.find('img', class_='img-fluid')['src']
    label = person_div.find('span', class_='badge').get_text()
    agent_info = person_div.find('div', class_='person-agent-info')
    agent_name = agent_info.find('a')['href']
    registration_date = agent_info.find('span', class_='d-block').get_text()
    return {
        'href': href,
        'img_src': img_src,
        'label': label,
        'agent_name': agent_name,
        'registration_date': registration_date
    }
def extract_registration_info(soup):
    registration_info = soup.find('div', class_='pagecontent')
    if registration_info:
        registration_data = {}
        for item in registration_info.find_all('li'):
            key = item.find('div', class_='view-th').text.strip()
            value = item.find('div', class_='view-td').text.strip()
            # Correcting the format for "失踪地点" field
            if '失踪地点' in key:
                value = key.split('：')[-1]
                key = '失踪地点：'
            registration_data[key] = value
        return registration_data
    else:
        print("Registration information not found.")
        return None
def scrape_page(page_number):
    url = f'https://www.baobeihuijia.com/bbhj/channels/3_{page_number}.html'
    html_content = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(html_content, 'html.parser')
    person_divs = soup.find_all('div', class_='person-image')
    for person_div in person_divs:
        person_info = extract_person_info(person_div)
        result_url = 'https://www.baobeihuijia.com' + person_info['href']
        result_html_content = requests.get(result_url).content.decode('utf-8')
        result_soup = BeautifulSoup(result_html_content, 'html.parser')
        registration_data = extract_registration_info(result_soup)
        if registration_data:
            with open('宝贝回家3.csv', 'a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(registration_data.values())
with open('宝贝回家3.csv', 'w', encoding='utf-8', newline='') as f:
        f.write("Title,寻亲类别：,失踪类型：,寻亲编号：,姓名：,性别：,出生日期：,失踪时身高：,失踪时间：,失踪地点,失踪者特征描述：,其他资料：,注册时间：,跟进志愿者：")
        f.write("\n")
# Iterate over pages from 2 to 5
for page_number in range(2, 200):
    scrape_page(page_number)