import json
class Transformer:

    def __init__(self, value):
        self.value = value

    def write_file(self):
        dat = open("test_4", 'w', encoding='utf-8')
        print(self.value, file=dat)
        print('Файл записан', self.value)
        dat.close()

    def open_file(self):
        dat = open("test_4", 'r', encoding='utf-8')
        self.value = Transformer.serialize_dict(dat.read())
        print('Файл считан и проеобразован', self.value, type(self.value))
        dat.close()

    def serialize_dict(x):
        return json.loads(x.replace("'",'"'))

    def __str__(self):
        return f"Конвертация dict-str-dict {self.value}"

operand = Transformer({'Go': 'home'})
print(operand)
operand.write_file()
operand.open_file()

class TransformerLegacy(Transformer):
    def __str__(self):
        return f"Конвертация dict-json {self.value}"

    def serialize_dict(self):
        self.value = json.dumps(self.value)
        return self.value

operand_2 = TransformerLegacy({'be':'healthy'})
print(operand_2)
print(operand_2.serialize_dict())

