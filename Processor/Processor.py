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

    def get_index(self):
        return self.__index