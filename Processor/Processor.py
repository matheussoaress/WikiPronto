import json
from urllib import request
from urllib import parse
"""
"  Processamento de indexação das informações do documento
"
"""

class Processor:

    def __init__(self):
        self.__index = {}

    """
    " Indexador
    " :param str doc
    " :param dict words
    """
    def indexer(self, doc, words):
        for word in words:
            if word not in self.__index:
                self.__index[word] = {}
            if doc not in self.__index[word]:
                self.__index[word][doc] = words[word]

    """
    " Retorna os index
    " :return dict
    """
    def get_index(self):
        return self.__index

    """
    " Fazer a consulta de index
    " :param list q
    """
    def query(self, q):
        res = []
        for index in q:
            if index in self.__index:
                res.append(self.__index[index])
        return res

    """
    " :param str text
    """
    def translate_pt_en(self, text):
        params = {"text": text, "options": 4}
        query = parse.urlencode(params)
        url = "https://translate.yandex.net/api/v1/tr.json/translate?id=9fd6cc5c.573e055a.5ce35796-10-0&srv=tr-text&lang=pt-en&reason=auto"
        req = request.build_opener()
        req.add_header = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]
        site = req.open(url, query)
        if site is not None and site.status == 200:
            return json.loads(site.read())
        return None
