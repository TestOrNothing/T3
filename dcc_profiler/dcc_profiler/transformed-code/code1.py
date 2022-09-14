def ladra_out(word):
    Profile.record('ladra_out', [word])
    print(word)

class Perro:

    def __init__(self):
        Profile.record('__init__', [self])
        self.name = 'perro'
        self.color = 'negro'

    def ladra(self, word):
        Profile.record('ladra', [self, word])
        print(word)

    def ladra2(self, word):
        Profile.record('ladra2', [self, word])
        ladra_out(word)
dog = Perro()
dog.ladra('hola')
dog.ladra2('hola')
dog.ladra2('hola')
dog.ladra2('hola')