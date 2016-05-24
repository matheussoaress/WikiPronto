import json
import requests
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
        try:
            if len(text) > 1:
                params = {"text": text, "options": 4}
                url = "https://translate.yandex.net/api/v1/tr.json/translate?id=9fd6cc5c.573e055a.5ce35796-10-0&srv=tr-text&lang=pt-en&reason=auto"
                r = requests.post(url, params)
                if r is not None and r.status_code == 200:
                    content = json.loads(r.text)
                    content = content['text']
                    return content[0]
            if text is None:
                text = ""
            return text
        except Exception as e:
            print(repr(e))
