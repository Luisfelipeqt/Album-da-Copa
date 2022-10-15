from People import Pessoa, No

       
class Album():
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir(self, dados):
        novo = No(dados)
        novo.proximo = self.inicio
        self.inicio = novo
        self.tamanho = self.tamanho + 1

        
    def buscar(self, dados):
        aux = self.inicio
        while aux is not None:
            if aux.dados == dados:
                print(f"O valor que você procura {aux.dados.list_data()} está na lista")
                return dados
            aux = aux.proximo
            

    def remover(self, dados):
        ultimo = self.inicio
        aux = self.inicio
        while aux is not None:
            if aux.dados == dados:
                ultimo.proximo = aux.proximo
                return aux
            aux = aux.proximo   

    def print_list(self):
        aux = self.inicio
        prnt_list = list()
        while aux is not None:
            prnt_list.append(aux.dados.list_data())
            aux = aux.proximo
        print(prnt_list)
        return prnt_list

    
                        
  
p = Pessoa("Felipe", 92, 1.65, "Brasil")
p1 = Pessoa("Laura", 60, 1.66, "Brasil")
p2 = Pessoa("Vanda", 68, 1.63, "Brasil")

Lista = Album()
Lista.inserir(p)
Lista.inserir(p1)
Lista.inserir(p2)
Lista.buscar(p)
Lista.buscar(p1)
Lista.buscar(p2)
Lista.print_list()











