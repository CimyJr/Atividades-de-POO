"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
from datetime       import date
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=date.today()   
        self._itens=[]
        self._valorNota=0.0        


    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

       
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor += item._valorItem
        self.valorNota=valor
     
    def imprimirNotaFiscal(self):       
        print("-" * 112)
        print("NOTA FISCAL", " " * 89, "{}/{}/{}".format(self._data.day, self._data.month, self._data.year))
        print("Cliente: {}    Nome: {}".format(self._cliente._id, self._cliente._nome))
        print("CPF/CNPJ: ", self._cliente._cnpjcpf)
        print("-" * 112)
        print("ITENS")
        print("-" * 112)
        print("Seq   Descrição", " " * 50, "QTD     Valor Unit              Preço" )
        print("---- ", "-" * 56, "   -----   ", "-" * 10, "      ", "-" * 19)
        for x in self._itens:
            print("{:0>3}    {:60}{}{:12}{:25.2f}".format(x.getSequencial(), x.getDescricao(), x.getQuantidade(), x.getUnitario(), x.getValorItem()))
        print("_" * 112)
        print("Valor Total: ", self.valorNota)
        pass