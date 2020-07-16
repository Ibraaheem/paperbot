import httplib2
import timeit
from bs4 import BeautifulSoup, SoupStrainer
from utils import utils
import re

class Sorter:

    def get_subjects(self, page_links):
        subjects = set()
        http = httplib2.Http()
        for page_link in page_links:
            status, response = http.request(page_link)
            for link in BeautifulSoup(response, parse_only=SoupStrainer('div', attrs={"class": "panel-heading"})):
                subjects.add(link.string.replace(' ', '%20'))
        return dict.fromkeys(subjects, [])

    def sort_by_language(self, papers):
        sorted_languages = []
        sorted_non_languages = []
        for paper in papers:
            if 'non-languages' in paper:
                sorted_non_languages.append(paper)
            elif 'non%s20languages' % ('%') in paper:
                sorted_non_languages.append(paper)
            else:
                sorted_languages.append(paper)
        return sorted_languages, sorted_non_languages
        
    def sort_by_subject(self, papers, subjects):
        sorted_subjects = subjects
        paper_by_subject = []
        for subject in sorted_subjects:
            for paper in papers:
                if subject in paper:
                    paper_by_subject.append(paper)
            sorted_subjects[subject] = paper_by_subject
            paper_by_subject = []
        return sorted_subjects
        

    def sort_valid_languages(self, papers, subjects):
        sorted_languages, sorted_non_languages = self.sort_by_language(papers)
        sorted_languages = self.sort_by_subject(list(sorted_languages),subjects)
        sorted_languages = dict( [(k,v) for k,v in sorted_languages.items() if len(v)>0])
        return sorted_languages

    def sort_non_languages(self, papers, subjects):
        sorted_languages, sorted_non_languages = self.sort_by_language(papers)
        sorted_non_languages = self.sort_by_subject(list(sorted_non_languages),subjects)
        sorted_non_languages = dict( [(k,v) for k,v in sorted_non_languages.items() if len(v)>0])
        return sorted_non_languages

    def get_sorted_papers(self, papers, subjects):
        languages, non_languages = self.sort_valid_languages(papers, subjects), self.sort_non_languages(papers, subjects)
        return {
            'languages': languages,
            'non_languages': non_languages
        }
        