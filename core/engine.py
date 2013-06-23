import urllib
import requests
from operator import itemgetter
from BeautifulSoup import BeautifulSoup


class KeywordAnalyzer(object):

    def __init__(self, keyword, language='es'):
        self.keyword = keyword
        self.language = language

    def run(self):
        self.suggestions = []
        for k in self._build_keywords(self.keyword):
            self.suggestions += self._get_suggestions(k, self.language)

        self.suggestions = list(set(self.suggestions))  # remove duplicates
        self.suggestions = sorted(self.suggestions, key=itemgetter(1), reverse=True)  # sort by rank
        return self

    def _build_keywords(self, keyword):
        ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
        return ('{} {}'.format(self.keyword, letter) for letter in ALPHABET)

    def _get_suggestions(self, keyword, language):
        BASE_URL = 'http://suggestqueries.google.com/complete/search'
        query = lambda s: s['data']
        rank = lambda s: int(s.findChild('num_queries')['int'])

        # Get Suggestions from Google
        params = urllib.urlencode({'output': 'toolbar', 'hl': language, 'q': keyword})
        res = requests.get('{}?{}'.format(BASE_URL, params))
        soup = BeautifulSoup(res.content)

        return map(lambda s: (query(s), rank(s)), soup.findAll('suggestion'))

# Cache de busquedas
