"""
"  Efetua o pré-processamento do documento.
"""


class Preprocessor:
    __stopwords = ()
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
