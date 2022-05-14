import matplotlib.pyplot as plt
import Sinal as sinal

class Impulso(sinal.Sinal):
    def __init__(self, sinal = {}):
        super().__init__(sinal)

    def criaSinalSomatorio(self, amplitude, deslocamento, objRange):
        """Cria um somatório de um sinal impulso
            amplitude: amplitude do sinal 
            deslocamento: funcao lambda para o deslocamento em cada
                iteração do somatório.
            objRange: espera um objeto iteravel com o intervalo do somatório
        """
        for i in objRange:
            self.sinal.update({deslocamento(i): amplitude})

    def __add__(self, aSomar):
        return super().__add__(aSomar)
            
    def plotSinal(self, nome="plot"):
        """
        Salva o sinal em pdf
        nome: nome do arquivo pdf (padrão: 'plot')
        """
        x = [key for key in self.sinal.keys()]
        y = [item for item in self.sinal.values()]
        fig, ax = plt.subplots(1,1)

        ax.stem(x, y, linefmt='b-',use_line_collection=True)
        ax.grid(True)
        ax.set_xlabel("Amostras")
        ax.set_xticks(x)
        ax.set_ylabel("Amplitude")
        
        fig.tight_layout()

        plt.savefig(f"{nome}.pdf")
