from dto.validation import validator

class Services:
    @classmethod
    def validResult(cls, campo, valore):
        return validator.validate(campo, valore)