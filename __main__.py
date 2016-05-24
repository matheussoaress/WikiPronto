import json
import time

from OsManager.FileManager import FileManager
from Processor.Preprocessor import Preprocessor
from Processor.HtmlContent import HtmlContent
from Processor.Processor import Processor


def get_file_name(path):
    a = path.split(".")
    b = a[0].split('\\')
    return b[len(b) - 1]


def indexer(process):
    fm = FileManager('I:\\docs')
    content = fm.get_next_content_file()
    while content is not None:
        print("Processando arquivo " + content[0])
        if content[1].find("<html") > -1:
            parser = HtmlContent()
            parser.feed(data=content[1])
            data = parser.content
        else:
            data = content[1]
        preproc = Preprocessor(content=data)
        process.indexer(content[0], preproc.get_words())
        content = fm.get_next_content_file()
    result = process.get_index()
    fm.save_result(result)
    return process


def query(process, q):
    files = process.query(['lula', 'dilma', 'pt', 'impeachment'])
    paths = []
    for keys in files:
        paths.append(keys.keys())
    aux = []
    for p in paths:
        for path in p:
            aux.append(path)
    return aux


def translate(process, path, c):
    tr_from = "\t\n"
    tr_to = "__"
    trans = str.maketrans(tr_from, tr_to)
    fm = FileManager()
    name = get_file_name(path)
    content = fm.get_file_content(path)
    parser = HtmlContent()
    parser.feed(data=content)
    data = parser.content
    text = ""
    for row in data:
        row = row.translate(trans)
        row = row.replace("_", "")
        row = row.strip()
        if row is not "":
            en_content = process.translate_pt_en(row)
            print(en_content)
            if en_content is not None:
                text += " " + en_content
    fm.save_result(text, name + " " + str(c))
    print("")


def get_links(path):
    try:
        fm = FileManager()
        content = fm.get_file_content(path)
        content = json.loads(content)
        paths = []
        for keys in content:
            paths.append(keys.keys())
        aux = []
        for p in paths:
            for path in p:
                aux.append(path)
        return aux
    except Exception as e:
        print(repr(e))


def main():
    process = Processor()
    links = get_links("I:\\docs\\result_links.json")
    c = 0
    for link in links:
        print(link)
        c += 1
        translate(process, link, c)
        time.sleep(30)


if __name__ == '__main__':
    main()

'''
'    :param str path
'''
