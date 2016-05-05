from NLTK3.Rslp import RSLPStemmer

"""
"  Efetua o pré-processamento do documento.
"""


class Preprocessor:
    __stopwords = ('a', 'à', 'agora', 'ainda', 'alguém', 'algum', 'alguma', 'algumas', 'alguns', 'ampla', 'amplas', 'amplo', 'amplos', 'ante', 'antes', 'ao', 'aos', 'após', 'aquela', 'aquelas', 'aquele', 'aqueles', 'aquilo', 'as', 'até', 'através', 'cada', 'coisa', 'coisas', 'com', 'como', 'contra', 'contudo', 'da', 'daquele', 'daqueles', 'das', 'de', 'dela', 'delas', 'dele', 'deles', 'depois', 'dessa', 'dessas', 'desse', 'desses', 'desta', 'destas', 'deste', 'deste', 'destes', 'deve', 'devem', 'devendo', 'dever', 'deverá', 'deverão', 'deveria', 'deveriam', 'devia', 'deviam', 'disse', 'disso', 'disto', 'dito', 'diz', 'dizem', 'do', 'dos', 'e', 'é', 'ela', 'elas', 'ele', 'eles', 'em', 'enquanto', 'entre', 'era', 'essa', 'essas', 'esse', 'esses', 'esta', 'está', 'estamos', 'estão', 'estas', 'estava', 'estavam', 'estávamos', 'este', 'estes', 'estou', 'eu', 'fazendo', 'fazer', 'feita', 'feitas', 'feito', 'feitos', 'foi', 'for', 'foram', 'fosse', 'fossem', 'grande', 'grandes', 'há', 'isso', 'isto', 'já', 'la', 'la', 'lá', 'lhe', 'lhes', 'lo', 'mas', 'me', 'mesma', 'mesmas', 'mesmo', 'mesmos', 'meu', 'meus', 'minha', 'minhas', 'muita', 'muitas', 'muito', 'muitos', 'na', 'não', 'nas', 'nem', 'nenhum', 'nessa', 'nessas', 'nesta', 'nestas', 'ninguém', 'no', 'nos', 'nós', 'nossa', 'nossas', 'nosso', 'nossos', 'num', 'numa', 'nunca', 'o', 'os', 'ou', 'outra', 'outras', 'outro', 'outros', 'para', 'pela', 'pelas', 'pelo', 'pelos', 'pequena', 'pequenas', 'pequeno', 'pequenos', 'per', 'perante', 'pode', 'pôde', 'podendo', 'poder', 'poderia', 'poderiam', 'podia', 'podiam', 'pois', 'por', 'porém', 'porque', 'posso', 'pouca', 'poucas', 'pouco', 'poucos', 'primeiro', 'primeiros', 'própria', 'próprias', 'próprio', 'próprios', 'quais', 'qual', 'quando', 'quanto', 'quantos', 'que', 'quem', 'são', 'se', 'seja', 'sejam', 'sem', 'sempre', 'sendo', 'será', 'serão', 'seu', 'seus', 'si', 'sido', 'só', 'sob', 'sobre', 'sua', 'suas', 'talvez', 'também', 'tampouco', 'te', 'tem', 'tendo', 'tenha', 'ter', 'teu', 'teus', 'ti', 'tido', 'tinha', 'tinham', 'toda', 'todas', 'todavia', 'todo', 'todos', 'tu', 'tua', 'tuas', 'tudo', 'última', 'últimas', 'último', 'últimos', 'um', 'uma', 'umas', 'uns', 'vendo', 'ver', 'vez', 'vindo', 'vir', 'vos', 'vós')
    __content = []
    __info = []

    """
    "  Inicia o preprocessamento da linguagem
    "  :param str[] content
    "  :return void
    """
    def __init__(self, content):
        self.__content = content

        for data in content:
            data = self.__data_encoder(data)
            data = self.__lexan(data)
            data = self.__remove_stopwords(data)
            self.__data = self.__remove_stemming(data)

    """
    " Decodifica a string para UTF-8
    " :param str data
    " :return str
    """
    def __data_encoder(self, data):
        return data.encode(encoding='UTF-8',errors='strict')

    """
    "  Desabilita caixa alta de todas as palavras.
    "  Remove os caracteres que não pertence ao vocabilário desejado
    "  Remove acentos
    "  :param str data
    "  :return str
    """
    def __lexan(self, data):
        trFrom = "ÁáÂâÀàÅåÃãÄäÆæÉéÊêÈèËëÐðÍíÎîÌìÏïÓóÔôÒòØøÕõÖöÚúÛûÙùÜüÇçÑñ®©ÝýÞþß'\"!@#$%¨&*()_+=-¹²³£¢¬§`{}^<>:?´[~],.;/ªº°"
        trTo = "AaAaAaAaAaAaEeEeEeEeEeEeIiIiIiIiOoOoOoOoOoOoUuUuUuUuCcNn_cYy__B________________123____________________aoo"
        trans = str.maketrans(trFrom, trTo)
        data = data.translate(trans)
        data = data.replace("_", "")
        return data.lower()

    """
    "  Remove as Stop Words do texto
    "  :param str data
    "  :return str
    """
    def __remove_stopwords(self, data):
        info = []
        data = data.split(" ")
        for word in data:
            if word not in self.__stopwords:
                info.append(word)

        data = ""
        for word in info:
            data+=word+" "
        return data

    def __remove_stemming(self, data):
        st = RSLPStemmer
        newData = []
        for word in data:
            if word is not "":
                newData.append(st.stem(word))
        return newData

    def get_result(self):
        return self.__data
