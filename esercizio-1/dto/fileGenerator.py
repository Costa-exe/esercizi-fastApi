class FileGen:
    @classmethod
    def textFile(cls, nomeFile, contenuto):
        with open(f"{nomeFile}.pdf", 'wb') as f:
            f.write(contenuto)
        
        return f"{nomeFile}.pdf"