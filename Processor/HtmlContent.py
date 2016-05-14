from html.parser import HTMLParser


class HtmlContent(HTMLParser):

    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.content = []

    def feed(self, data):
        super().feed(data)

    def handle_data(self, data):
        if data != '':
            self.content.append(data)

    def error(self, message):
        print(message)