import re

class validator:
    @classmethod
    def validate(cls, campo, valore):
        match campo:
            case "IdAnagrafica":
                if not re.search("^[0-9]{9}$", str(valore)):
                    return "KO"
                else:
                    return valore
            case "CF":
                if not re.search("^([A-Z]{6}[0-9LMNPQRSTUV]{2}[ABCDEHLMPRST]{1}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{3}[A-Z]{1})$|([0-9]{11})$", valore):
                    return "KO"
            case "email":
                if not re.search("^[aA-zZ0-9._-]+@[aA-zZ0-9.-]+.[aA-zZ]{2,4}$", valore):
                    return "KO"
            case "numTel":
                valore = str(valore).replace(" ", "")
                if not re.search("^[0-9]{10}$|^[0-9]{9}$", valore):
                    return "KO"