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
        assert self.inicio, "Impossivel remover de lista vazia!"

        if self.inicio.dados == dados:
            self.inicio = self.inicio.proximo
        else:

            anterior = None
            corrente = self.inicio

            while corrente and corrente.dados != dados:
                anterior = corrente
                corrente = corrente.proximo
            
            if corrente:
                anterior.proximo = corrente.proximo
            else:
                print("Não está na lista")
        self.tamanho = self.tamanho - 1


    def print_list(self):
        aux = self.inicio
        prnt_list= list()  
        while aux is not None:
            prnt_list.append(aux.dados.list_data())
            aux = aux.proximo
        x = prnt_list
        a = sorted(x)
        print(prnt_list)
        return prnt_list

    def print_list_sorted(self):
        aux = self.inicio
        prnt_list= list()  
        while aux is not None:
            prnt_list.append(aux.dados.list_data())
            aux = aux.proximo
        x = prnt_list
        a = sorted(x)
        print(a)
        return prnt_list

    
                        
  
p = Pessoa("Felipe", 92, 1.65, "França")
p1 = Pessoa("Laura", 60, 1.66, "America")
p2 = Pessoa("Vanda", 68, 1.63, "México")


Lista = Album()
Lista.inserir(p)
Lista.inserir(p1)
Lista.inserir(p2)
Lista.remover(p1)
Lista.print_list()
Lista.print_list_sorted()