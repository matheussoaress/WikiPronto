from OsManager.FileManager import FileManager
from Processor.Preprocessor import Preprocessor
from Processor.HtmlContent import HtmlContent
from Processor.Processor import Processor


def main():
    try:
        fm = FileManager('D:\\Trabalhos_Praticos\\Recuperação de Informação\\wikiSample\\')
        process = Processor()
        content = fm.get_next_content_file()
        while content is not None:
            parser = HtmlContent()
            parser.feed(data=content[1])
            data = parser.content
            preproc = Preprocessor(content=data)
            process.indexer(content[0], preproc.get_words())
            content = fm.get_next_content_file()
        print(process.get_index())
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    main()