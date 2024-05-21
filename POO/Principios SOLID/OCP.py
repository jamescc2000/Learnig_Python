##################### Open / Close Principle ####################################
# Las entidades de software (Clases, modulos, funciones, etc) tiene que estar
# abierta para la extencion pero cerradas para la modificacion
# Es decir, deberiamos poder agregar nuevas funcionalidades sin cambiar el codigo fuente

class Notificacdor():
    def __init__(self, usuario, mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificacdor):
    def notificar(self):
        print(f'Enviando mensaje por mail a: {self.usuario.email}')
        
class NotificadorSMS(Notificacdor):
    def notificar(self):
        print(f'Enviando SMS a: {self.usuario.sms}')
        
class NotificadorWhatsapp(Notificacdor):
    def notificar(self):
        print(f'Enviando Whatsapp a: {self.usuario.whatsapp}')
           
