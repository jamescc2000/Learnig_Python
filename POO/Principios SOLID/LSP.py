##################### Liskov's Substitution Principle ####################################
# Las clases derivadas tiene que ser sustituibles por sus clases bases

# class Ave:
#     def volar(self):
#         return 'Estoy volando'
    
# class Pinguino(Ave):
#     def volar(self):
#         return 'No puedo volar'
    

# def hacer_volar(ave=Ave):
#     return ave.volar()


# print(hacer_volar(Pinguino()))

class Ave:
    pass

class Avevoladora(Ave):
    def volar(self):
        return 'Estoy volando'
    
class AveNoVoldora(Ave):
    def volar(self):
        pass