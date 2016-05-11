import operator

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
        words = sorted(self._words.items(), key=operator.itemgetter(1), reverse=True)
        self.__tree = CompressorBinaryTree
        a = self.__tree
        for word in words:
            a.leftTree = word
            a.rightTree = CompressorBinaryTree
            a = a.rightTree

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
    key = 0
