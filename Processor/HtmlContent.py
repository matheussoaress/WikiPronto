from html.parser import HTMLParser


class HtmlContent(HTMLParser):
    __content = []

    def handle_starttag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if data != '':
            self.__content.append(data)

    def error(self, message):
        print(message)