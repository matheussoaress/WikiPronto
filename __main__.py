from OsManager.FileManager import FileManager
import Processor

def main():
    fm = FileManager('D:\Trabalhos Praticos\Recuperação de Informação\wikiSample')
    files = fm.getFiles()
    for file in files:
        print(file)

if __name__ == '__main__':
    main()