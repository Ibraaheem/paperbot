import httplib2
import timeit
from bs4 import BeautifulSoup, SoupStrainer
from utils import utils
import re

class Sorter:

    """
    sort sequence:
    - year
    - language
    - subject
    """

    def sort_by_language(self, papers):
        languages = []
        non_languages = []
        for paper in papers:
            if 'non-languages' in paper:
                non_languages.append(paper)
            else:
                languages.append(paper)
        return languages, non_languages

    def get_subjects(self, url):
        subjects = set()
        http = httplib2.Http()
        status, response = http.request(url)
        for link in BeautifulSoup(response, parse_only=SoupStrainer('div', attrs={"class": "panel-heading"})):
            subjects.add(link.string.replace(' ', '%20'))
        return dict.fromkeys(subjects, [])

    def sort_by_subject(self, papers, url):
        subjects = self.get_subjects(url)
        paper_by_subject = []
        for subject in subjects:
            for paper in papers:
                if subject in paper:
                    paper_by_subject.append(paper)
            subjects[subject] = paper_by_subject
            paper_by_subject = []
        return subjects
        

    def sort_by_year(self, sorted_papers):
        """
        papers_by_year = {
            "2020" : ['link','link','link',],
            "2019" : ['link','link','link',],
            ...
            }
        """
        years = set()
        sorted_subject = []
        languages = []
        non_languages = []
        for subject, papers in sorted_papers.items():
            for paper in papers:
                year = re.search(r'[12]\d{3}', paper).group(0)
                years.add(year)
        years = dict.fromkeys(years, '')

        for subject, papers in sorted_papers.items():
            for sub in subject:

                
        

        # for year in years:
        #     sorted_languages = []
        #     sorted_non_languages = []
        #     for lang in languages:
        #         if year in lang:
        #             sorted_languages.append(lang)
        #     for nlang in non_languages:
        #         if year in nlang:
        #             sorted_non_languages.append(nlang)
        #     years[year] = [sorted_languages, sorted_non_languages]
        
        # print(years['2016'])

