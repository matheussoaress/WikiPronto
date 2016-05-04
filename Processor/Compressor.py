import os

"""
"  Comprime e descomprime os documentos
"""


class Compressor:
    __orig_content = []
    __words = {}

    def __init__(self, content):
        __orig_content = content

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

    def statist_compressor(self):
        pass

class CompressorBinaryTree:
    leftTree = None
    rightTree = None