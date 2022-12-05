from byteTranslate import byteTranslator

class FileGen:
    @classmethod
    def textFile(cls, nomeFile, contenuto):
        with open(f"{nomeFile}.txt", 'w') as f:
            f.write(contenuto)
        
        return f"{nomeFile}.txt"