class byteTranslator:
    @classmethod
    def translator(cls, string):
        return bytearray(string, 'utf8')
