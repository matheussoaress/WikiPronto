#from NLTK3.Rslp import RSLPStemmer
import nltk
"""
"  Efetua o pré-processamento do documento.
"""


class Preprocessor:
    __stopwords = ('a', 'à', 'agora', 'ainda', 'alguém', 'algum', 'alguma', 'algumas', 'alguns', 'ampla', 'amplas', 'amplo', 'amplos', 'ante', 'antes', 'ao', 'aos', 'após', 'aquela', 'aquelas', 'aquele', 'aqueles', 'aquilo', 'as', 'até', 'através', 'cada', 'coisa', 'coisas', 'com', 'como', 'contra', 'contudo', 'da', 'daquele', 'daqueles', 'das', 'de', 'dela', 'delas', 'dele', 'deles', 'depois', 'dessa', 'dessas', 'desse', 'desses', 'desta', 'destas', 'deste', 'deste', 'destes', 'deve', 'devem', 'devendo', 'dever', 'deverá', 'deverão', 'deveria', 'deveriam', 'devia', 'deviam', 'disse', 'disso', 'disto', 'dito', 'diz', 'dizem', 'do', 'dos', 'e', 'é', 'ela', 'elas', 'ele', 'eles', 'em', 'enquanto', 'entre', 'era', 'essa', 'essas', 'esse', 'esses', 'esta', 'está', 'estamos', 'estão', 'estas', 'estava', 'estavam', 'estávamos', 'este', 'estes', 'estou', 'eu', 'fazendo', 'fazer', 'feita', 'feitas', 'feito', 'feitos', 'foi', 'for', 'foram', 'fosse', 'fossem', 'grande', 'grandes', 'há', 'isso', 'isto', 'já', 'la', 'la', 'lá', 'lhe', 'lhes', 'lo', 'mas', 'me', 'mesma', 'mesmas', 'mesmo', 'mesmos', 'meu', 'meus', 'minha', 'minhas', 'muita', 'muitas', 'muito', 'muitos', 'na', 'não', 'nas', 'nem', 'nenhum', 'nessa', 'nessas', 'nesta', 'nestas', 'ninguém', 'no', 'nos', 'nós', 'nossa', 'nossas', 'nosso', 'nossos', 'num', 'numa', 'nunca', 'o', 'os', 'ou', 'outra', 'outras', 'outro', 'outros', 'para', 'pela', 'pelas', 'pelo', 'pelos', 'pequena', 'pequenas', 'pequeno', 'pequenos', 'per', 'perante', 'pode', 'pôde', 'podendo', 'poder', 'poderia', 'poderiam', 'podia', 'podiam', 'pois', 'por', 'porém', 'porque', 'posso', 'pouca', 'poucas', 'pouco', 'poucos', 'primeiro', 'primeiros', 'própria', 'próprias', 'próprio', 'próprios', 'quais', 'qual', 'quando', 'quanto', 'quantos', 'que', 'quem', 'são', 'se', 'seja', 'sejam', 'sem', 'sempre', 'sendo', 'será', 'serão', 'seu', 'seus', 'si', 'sido', 'só', 'sob', 'sobre', 'sua', 'suas', 'talvez', 'também', 'tampouco', 'te', 'tem', 'tendo', 'tenha', 'ter', 'teu', 'teus', 'ti', 'tido', 'tinha', 'tinham', 'toda', 'todas', 'todavia', 'todo', 'todos', 'tu', 'tua', 'tuas', 'tudo', 'última', 'últimas', 'último', 'últimos', 'um', 'uma', 'umas', 'uns', 'vendo', 'ver', 'vez', 'vindo', 'vir', 'vos', 'vós')
    __content = []
    __words = {}
    __stem_words ={}

    """
    "  Inicia o preprocessamento da linguagem
    "  :param str[] content
    "  :return void
    """
    def __init__(self, content):
        self.__content = content

        words = {}
        c = 0
        for data in content:
            data = self.__data_encoder(data) if type(data) is bytes else data
            data = self.__lexan(data)
            if data != "":
                all_words = data.split(" ")
                for word in all_words:
                    if word != "":
                        c += 1
                        if word not in words:
                            words[word] = []
                        words[word].append(c)
        self.__remove_stopwords(words)
        self.__remove_stemming()


    """
    " Decodifica a string para UTF-8
    " :param str data
    " :return str
    """
    def __data_encoder(self, data):
        #data = data.encode(encoding='UTF-8',errors='strict')
        return data.decode('utf-8', 'ignore')

    """
    "  Desabilita caixa alta de todas as palavras.
    "  Remove os caracteres que não pertence ao vocabilário desejado
    "  Remove acentos
    "  :param str data
    "  :return str
    """
    def __lexan(self, data):
        trFrom = "ÁáÂâÀàÅåÃãÄäÆæÉéÊêÈèËëÐðÍíÎîÌìÏïÓóÔôÒòØøÕõÖöÚúÛûÙùÜüÇçÑñ®©ÝýÞþß'\"!@#$%¨&*()_+=-¹²³£¢¬§`{}^<>:?´[~],.;/ªº°\t\n|"
        trTo = "AaAaAaAaAaAaEeEeEeEeEeEeIiIiIiIiOoOoOoOoOoOoUuUuUuUuCcNn_cYy__B________________123____________________aoo___"
        trans = str.maketrans(trFrom, trTo)
        data = data.translate(trans)
        data = data.replace("_", "")
        return data.lower()

    """
    "  Remove as Stop Words do texto
    "  :param dict data
    "  :return None
    """
    def __remove_stopwords(self, data):
        info = data.copy()
        for word in data:
            if word in self.__stopwords:
                info.pop(word)
        if "" in info:
            info.pop("")
        self.__words = info

    """
    " Remove as stemming das palavras
    " :param dict data
    " :return None
    """
    def __remove_stemming(self):
        #st = RSLPStemmer()
        stemmer = nltk.stem.RSLPStemmer()
        stem_words = {}
        for word in self.__words:
            stem_word = stemmer.stem(word)
            if stem_word not in stem_words:
                stem_words[stem_word] = self.__words[word]
        self.__stem_words = stem_words

    def get_words(self):
        return self.__words

    def get_stem_words(self):
        return self.__stem_words

