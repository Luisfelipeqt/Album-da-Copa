from Node import No

class Pessoa():   
    def __init__(self, nome, peso, altura, selecao):
        self.nome = nome     
        self.peso = peso
        self.altura = altura
        self.selecao = selecao


    def list_data(self):
        return {
            "nome": self.nome,
            "peso": self.peso,
            "altura": self.altura,
            "selecao": self.selecao
        }
        