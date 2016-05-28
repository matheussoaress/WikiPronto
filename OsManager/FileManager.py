import json
from datetime import datetime
import os


class FileManager:
    __files = []
    __names = []
    __n = 0

    def __init__(self, root):
        self.__getFilePath(root)

    def get_file(self, idx):
        try:
            content = None
            if len(self.__files) > idx:
                now = datetime.now()
                print(str(now.day)+"/"+str(now.month)+"/"+str(now.year)+" "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+"\tLendo arquivo: "+self.__files[idx])
                try:
                    with open(self.__files[idx], 'r') as fp:
                        content = fp.read()
                        fp.close()
                    return [self.__names[idx], content]
                except Exception as e:
                    try:
                        with open(self.__files[idx], 'rb') as fp:
                            content = fp.read()
                            fp.close()
                        return [self.__names[idx], content.decode()]
                    except Exception as e:
                        raise e
            else:
                return None
        except Exception as e:
            print(repr(e))

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
            now = datetime.now()
            print(str(now.day)+"/"+str(now.month)+"/"+str(now.year)+" "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+"\tLendo pasta: "+root)
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

    def save_json_result(self, path, data):
        try:
            data = json.dumps(data)
            path += os.sep+'result.json'
            with open(path, 'w') as fp:
                fp.write(data)
                fp.close()
        except Exception as e:
            print(repr(e))