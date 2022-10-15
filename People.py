from Node import No

class Pessoa():   
    def __init__(self, nome, peso, altura, selecao):
        self.selecao = selecao
        self.nome = nome     
        self.peso = peso
        self.altura = altura
        


    def list_data(self):
        return   [self.selecao,
                 self.nome,
                 self.peso,
                 self.altura,]
                
        
             
        
        