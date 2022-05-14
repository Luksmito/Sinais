
class Sinal():
    """Super class to deal with Signals"""
    def __init__(self, sinal = {}):
        self.sinal = sinal
    
    def __add__(self, aSomar):
        """Implementa uma sobrecarga do operador + para somar self.sinal"""
        sinal = {}
        sinal1 = self.sinal
        sinal2 = aSomar.sinal
        for key, item in sinal1.items():
            if key in sinal2.keys():
                sinal.update({key: sinal2[key] + item})
            else:
                sinal.update({key: item})
        for key, item in sinal2.items():
            if key in sinal1.keys():
                sinal.update({key: sinal1[key] + item})
            else:
                sinal.update({key: item})
        return sinal