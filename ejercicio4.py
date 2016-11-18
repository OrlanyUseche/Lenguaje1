class voltear:
    def __init__(self, oracion):
        self.oracion=str(oracion)     
    def convertir(self):
        frase = self.oracion.split();
        frase.reverse()
        oracion = ''
        for i in frase:
            oracion = oracion +' ' +i
        print oracion
palabras = voltear('orlany useche')
palabras.convertir()
