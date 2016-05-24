import json
import os


class FileManager:
    __files = []
    __names = []
    __n = 0

    def __init__(self, root=None):
        if root is not None:
            self.__root = root
            self.__getFilePath(root)
        else:
            self.__root = root=""

    def get_file(self, idx):
        try:
            content = None
            if len(self.__files) > idx:
                if self.__files[idx].find('.pdf') == -1 and self.__files[idx].find('.jpg') == -1 and self.__files[idx].find('.png') == -1 and self.__files[idx].find('.gif') == -1:
                    content = self.get_file_content(self.__files[idx])
                    return [self.__files[idx], content]
                else:
                    return self.get_file(idx+1)
            else:
                return None
        except Exception as e:
            print(repr(e))

    def get_file_content(self, path):
        fo = 'rb' if path.find('.dtpn') > -1 else 'r'
        with open(path, fo) as fp:
            content = fp.read()
            fp.close()
        return content.decode() if type(content) is bytes else content;

    def get_next_content_file(self):
        content = self.get_file(self.__n)
        self.__n += 1
        return content

    def get_prev_content_file(self):
        content = self.get_file(self.__n-1)
        self.__n += 1
        return content

    def __getFilePath(self, root):
        try:
            paths = os.listdir(root)
            for path in paths:
                aux = root+os.sep+path
                if os.path.isfile(aux) and aux not in self.__files:
                    self.__files.append(aux)
                    self.__names.append(path)
                if os.path.isdir(aux):
                    self.__getFilePath(aux)
        except Exception as e:
            print(repr(e))


    def getFiles(self):
        return self.__files

    def save_result(self, content, name=''):
        try:
            result = json.dumps(content)
            with open(self.__root+os.sep+"result_"+name+".json", 'w') as fp:
                fp.write(result)
                fp.close()
        except Exception as e:
            print(repr(e))