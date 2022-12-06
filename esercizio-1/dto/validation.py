import re

class validator:
    @classmethod
    def validate(cls, campo, valore):
        match campo:
            case "IdAnagrafica":
                return valore
            case "CF":
                valore = valore.upper()
                if not re.search("^([A-Z]{6}[0-9LMNPQRSTUV]{2}[ABCDEHLMPRST]{1}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{3}[A-Z]{1})$|([0-9]{11})$", valore):
                    return 'Not Valid'
                else:
                    return valore
            case "email":
                if not re.search("^[aA-zZ0-9._-]+@[aA-zZ0-9.-]+.[aA-zZ]{2,4}$", valore):
                    return "Not Valid"
                else:
                    return valore
            case "numTel":
                valore = str(valore).replace(" ", "")
                if not re.search("^[0-9]{10}$|^[0-9]{9}$", valore):
                    return "Not Valid"
                else:
                    return valore