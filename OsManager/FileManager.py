import os


class FileManager:
    __files = []

    def __init__(self, root):
        self.__getFilePath(root)

    def get_next_content_file(self, idx):
        try:
            content = None
            if len(self.__files) > idx:
                with open(self.__files[idx]) as fp:
                    content = fp.read()
                    fp.close()
            return content
        except Exception as e:
            print(repr(e))

    def __getFilePath(self, root):
        try:
            paths = os.listdir(root)
            for path in paths:
                aux = root+os.sep+path
                if os.path.isfile(aux) and aux not in self.__files:
                    self.__files.append(aux)
                if os.path.isdir(aux):
                    self.__getFilePath(aux)
        except Exception as e:
            print(repr(e))


    def getFiles(self):
        return self.__files;