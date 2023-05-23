import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import json
import csv

# person_url_list = []
#
# for i in range(0, 69, 10):
#     url = f"https://www.belarusinfo.by/ru/company/promyshlennost/otopitelnoe-oborudovanie.html?limitstart={i}"
#
#     q = requests.get(url)
#     result = q.content
#
#     soup = BeautifulSoup(result, "lxml")
#     person = soup.find_all(class_="s_c_title")
#
#     for person in person:
#         person_a = person.find("a")
#
#         person_page_url = person_a.get("href")
#         person_url_list.append(person_page_url)
#
# with open("person_url_list.txt", "a") as  file:
#     for line in person_url_list:
#         file.write(f"https://www.belarusinfo.by{line}\n")

# count = 0
#
# with open("person_url_list.txt") as file:
#     lines = [line.strip() for line in file.readlines()]
#
#     data_dict = []
#
#     for line in lines:
#
#         q = requests.get(line)
#         result = q.content
#
#         soup = BeautifulSoup(result, "lxml")
#         company_name = soup.find(class_="section-hero__title").text
#         company_role = soup.find(class_="section-hero__excerpt").find("h2").text
#         company_address = soup.find(class_="section-hero__sidebar").find("ul").find("li").find("address").text.strip()
#         block_phones = soup.find(class_="section-hero__phones js__company-phones").find("ul").find_all("a")
#         phone_list = []
#         for phone in block_phones:
#             phone_number = phone.get("data-real-phone")
#             phone_list.append(phone_number)
#
#         company_name_internet_href = []
#         email_and_site = []
#         company_email = soup.find(class_="section-hero__sidebar", id='page_contacts').find_all("ul")
#         for item in company_email:
#             a = item.find_all("a")
#             for href_a in a:
#                 b = href_a.get("href")
#                 if b == "#":
#                     continue
#                 company_name_internet_href.append(b)
#         for href in company_name_internet_href:
#             actual_href = href.replace("mailto:", "")
#             email_and_site.append(actual_href)
#
#         list_all_comapny_items = {
#             "Название компании: ": company_name,
#             "Деятельность компании: ": company_role,
#             "Адрес компании: ": company_address,
#             "Контактные телефоны компании: ": phone_list,
#             "Интернет почта и сайт компании: ": email_and_site
#         }
#
#         data_dict.append(list_all_comapny_items)
#         count = count + 1
#         print(count)
#
#         # with open("data_dict.json", "w", encoding="utf-8") as json_file:
#         #     json.dump(data_dict, json_file, indent=4)
#
#         with open(f"data_dict.csv", "a", encoding="utf-8") as file:
#             writer = csv.writer(file)
#             writer.writerow(
#                 (
#                     company_name,
#                     company_role,
#                     company_address,
#                     phone_list,
#                     email_and_site
#                 )
#             )
# print(data_dict)



