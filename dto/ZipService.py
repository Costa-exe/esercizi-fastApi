from zipfile import ZipFile

class Zipper :
    @classmethod
    def ZipNewFile(cls, file):
        with ZipFile('nuovoFile.zip', 'w') as newZip:
            newZip.write(file)

        return 'nuovoFile.zip'