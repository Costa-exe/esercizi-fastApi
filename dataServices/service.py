from dto.byteTranslate import byteTranslator
from dto.fileGenerator import FileGen
from dto.ZipService import Zipper
from dto.validation import validator

class Services:

    @classmethod
    def bytes(cls, string):
        return byteTranslator.translator(string)

    @classmethod
    def FileGenerate(cls, nomeFile, contenuto):
        return FileGen.textFile(nomeFile, contenuto)

    @classmethod
    def zip(cls, file):
        return Zipper.ZipNewFile(file)

    @classmethod
    def validResult(cls, campo, valore):
        return validator.validate(campo, valore)