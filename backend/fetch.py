import httplib2
import timeit
from bs4 import BeautifulSoup, SoupStrainer
from utils import utils, firebase
import re

start = timeit.default_timer()

url = 'https://wcedonline.westerncape.gov.za/grade-12-question-papers'
http = httplib2.Http()
status, response = http.request(url)
sorter = utils.Sorter()
db = firebase.UpdateDB()

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

subjects = sorter.get_subjects(page_links)
data = sorter.get_sorted_papers(papers_links, subjects)
db.send(data)

print("\n\n\n")
stop = timeit.default_timer()

print('Time: ', stop - start) 