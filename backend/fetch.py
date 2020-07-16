import httplib2
import timeit
from bs4 import BeautifulSoup, SoupStrainer
from utils import utils
import re

start = timeit.default_timer()

url = 'https://wcedonline.westerncape.gov.za/grade-12-question-papers'
http = httplib2.Http()
status, response = http.request(url)

page_links = []
papers_links = []

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        check_link = link['href']
        if 'nsc-examinations' in check_link:  
            page_links.append(check_link)

for page in page_links:
    status, response = http.request(page)
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            paper_link = link['href']
            if '.pdf' in paper_link:  
                papers_links.append(paper_link)

countl, countn = 0 , 0

languages, non_languages = utils.Sorter().sort_by_language(papers_links)
print("languages: \n")
# print(utils.Sorter().sort_by_year(languages))
# print(countl)
# print("\n\n\n")
# print("non-languages: \n")
# for nonlang in non_languages:
#     print(nonlang) 
#     countn += 1
# print(countn)
pap = utils.Sorter().sort_by_subject(papers_links, 'https://wcedonline.westerncape.gov.za/november-2018-nsc-examinations')
utils.Sorter().sort_by_year(pap)

print("\n\n\n")
stop = timeit.default_timer()

print('Time: ', stop - start) 