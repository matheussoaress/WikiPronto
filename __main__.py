from OsManager.FileManager import FileManager
from Processor.Preprocessor import Preprocessor
from Processor.HtmlContent import HtmlContent
from Processor.Processor import Processor


def main():
    fm = FileManager('I:\\docs')
    process = Processor()
    content = fm.get_next_content_file()
    while content is not None:
        print("Processando arquivo "+content[0])
        if content[1].find("<html") > -1:
            parser = HtmlContent()
            parser.feed(data=content[1])
            data = parser.content
        else:
            data = content[1]
        preproc = Preprocessor(content=data)
        process.indexer(content[0], preproc.get_words())
        content = fm.get_next_content_file()
    files = process.query(['lula', 'dima', 'pt', 'impeachment']).keys()
    paths=[]
    for keys in :
        paths.append(keys)
    fm.get_file_content()
    result = process.get_index()
    fm.save_result(result)


if __name__ == '__main__':
    main()

'''
'    :param fm FileManager
'    :param Process process
'    :param list q
'''
def translate( fm, process, q):
    files = process.query(q)
    for file in files:
        fm.get_file_content(file)