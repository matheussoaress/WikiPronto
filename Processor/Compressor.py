import os

"""
"  Comprime e descomprime os documentos
"""


class Compressor:
    _orig_content = []
    _words = {}

    def __init__(self, content):
        __orig_content = content
        self.__set_words()

    def __set_words(self):
        content = []
        for line in self.__orig_content:
            line = line.split(" ")
            for word in line:
                if word is not "":
                    content.append(word)
        for word in content:
            if word not in self.__words:
                self.__words[word] = 1
            else:
                self.__words[word]+=1


class StatisticCompressor( Compressor):

    def __init__(self, content):
        super.__init__(self, content)

    def statist_compressor(self):
        pass

class TableCompressor( Compressor):
    __table = {}

    def __init__(self, content):
        super.__init__(self, content)
        cont = 0
        for word in self._words:
            if word not in self.__table:
                self.__table[word] = cont
                cont+=1


class CompressorBinaryTree:
    leftTree = None
    rightTree = None