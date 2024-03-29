import requests
from bs4 import BeautifulSoup
import json

# person_url_list = []
#
# for i in range(0, 746, 24):
#     url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}"
#
#
#     q = requests.get(url)
#     result = q.content
#
#     soup = BeautifulSoup(result, "lxml")
#     person = soup.find(class_="bt-slide-content").find("a")
#     for pers in person:
#         person_page_url = person.get("href")
#         person_url_list.append(person_page_url)
#
# with open("person_url_list.txt", "a") as file:
#     for line in person_url_list:
#         file.write(f'{line}\n')

with open("person_url_list.txt") as file:
    lines =  [line.strip() for line in file.readlines()]
    date_dict = []
    count = 0
    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, "lxml")
        person =  soup.find(class_="bt-biografie-name").find("h3").text
        person_name_company = person.strip().split(",")
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_="bt-link-extern")

        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get("href"))

        data = {
            "person_name": person_name,
            "company_name": person_company,
            "social_networks": social_networks_urls
        }
        count += 1
        print(f"#{count}: {line} is done")

        date_dict.append(data)

        with open("data.json", "w") as json_file:
            json.dump(date_dict, json_file, indent=4)



