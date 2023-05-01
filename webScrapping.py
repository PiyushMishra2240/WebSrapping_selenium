from bs4 import BeautifulSoup
import requests

# with open('BeautifulSoupParser.html', 'r') as BeautifulSoupParser:
#     content = BeautifulSoupParser.read()
#     # print(content)

#     soup = BeautifulSoup(content, 'lxml') # parsing the contents as strings
#     # print(soup.prettify()) # to print the content in a pretty manner
#     # print(soup)
#     head_cards = soup.find_all('div', class_ = 'section')
#     for head_card in head_cards:
#         head_name = head_card.h1.text.split()[-1]
#         print(head_name)



html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li',  class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:

    published_date = job.find('span', class_ = 'sim-posted').text
    if 'few' in published_date:
        company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        # job_link = job.header.h2.a["href"]
        job_link = job.find('a')["href"]

        print(f"Company Name: {company_name.strip()}")
        print(f"SKills: {skills.strip()}")
        print(f"Job Link: {job_link}")
        
        print('\n')

# print(company_name)
# print(skills)
# print(published_date)