import requests
from bs4 import BeautifulSoup
import lxml
from proxy_auth import proxies
import json


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
# collect all fests URLs
fests_urls_lists = []
# for i in range(0, 229,  24):
for i in range(0, 24,  24):
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=&to_date=&maxprice=500&o={i}&bannertitle=May"

    req = requests.get(url=url, headers=headers, proxies=proxies)
    json_data = json.loads(req.text)
    html_responce = json_data['html']

    with open(f"data/index_{i}.html", "w") as file:
        file.write(html_responce)

    with open(f"data/index_{i}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    cards = soup.find_all("a", class_="card-details-link")

    for item in cards:
        fests_url = "https://www.skiddle.com/" + item.get("href")
        fests_urls_lists.append(fests_url)

#collect fest info

for url in fests_urls_lists[0:1]:
    req = requests.get(url=url, headers=headers, proxies=proxies)

    try:
        soup = BeautifulSoup(req.text, "lxml")
        fest_info_block = soup.find("div", class_="top-info-cont")

        fest_name = fest_info_block.find("h1").text.strip()
        faste_date = fest_info_block.find("h3").text.strip()
        fest_location_url = "https://www.skiddle.com/" + fest_info_block.find("a", class_="tc-white").get("href")

        # get contact details and info
        req = requests.get(url=fest_location_url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(req.text, "lxml")

        contact_details = soup.find("h2", string="Venue contact detail and info").find_next()
        items = [item.text for item in contact_details.find_all('p')]

        for contact_details in items:
            print(contact_details)
    except Exception as ex:
        print(ex)
        print("Damn.... There was some error....")


