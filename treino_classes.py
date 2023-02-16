class Conta:
    def __init__(self,numero,titular, saldo,limite):
        print(f'construindo objeto {self}')
        self.__numero = numero # O __ é um aviso para o desenvolvedor saber que nao deve manusear o atributo fora da classe
        self.__titular = titular # O __ é um aviso para o desenvolvedor saber que nao deve manusear o atributo fora da classe
        self.__saldo = saldo # O __ é um aviso para o desenvolvedor saber que nao deve manusear o atributo fora da classe
        self.__limite = limite # O __ é um aviso para o desenvolvedor saber que nao deve manusear o atributo fora da classe
        self.__codigo_banco = '001'

    def extrato(self):
        print(f'O Saldo da sua conta é:"{self.saldo} {self.titular}')

    def deposita(self,valor):
        self.saldo += valor

    def __pode_sacar(self,valor_sacar): # verificacao
        valor_disponivel = (self.__limite + self.__saldo)
        return valor_sacar <= valor_disponivel

    def saca(self,valor):
        if (self.__pode_sacar(valor)):
            self.saldo -= valor
        else:
            print(f'O seu valor {valor} passou o limite permitido')

    def transfere(self, valor, destino): #(Self,valor,origem, destino). Elimina a origem e mantem somente self e destino com o valor. evita redundancia
        self.saca(valor) # eliminando a origem mantem apenas o self pois vai apontar para a conta de origem que esta usando o metodo.
        destino.deposita(valor) # destino executando o metodo deposita com o valor
        #conta2.transfere(100,conta1)
        #encapsulado operacao criando um metodo na classe Conta.
        #organizacao, legibilidade e manutencao do codigo.

    # def inadimplente(self):
    # Cuidado ao criar um metodo que nao pertence a essa classe, inadimplencia seria um metodo que nao esta na classe /Conta/
    # Manter coesao do paradigma orientado a objeto.
    # SOLID
    '''
    def get_saldo(self):    #retornar o valor do atributo
        return self.__saldo #atributo sendo manipulado dentro da classe.

    def get_titular(self):    #retornar o valor do atributo
        return self.__titular #atributo sendo manipulado dentro da classe.

    def get__limite(self):   #retornar o valor do atributo
        return self.__limite #atributo sendo manipulado dentro da classe.

    def get__numero(self): #retornar o valor do atributo
        return self.__numero #atributo sendo manipulado dentro da classe.
    def set__limite(self, limite): #set de valor do atributo.
        self.__limite = limite #atributo sendo manipulado dentro da classe.'''
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):  # Deixar o get mais amigavel com o desenvolvedor
        return self.__limite
        # getters
        # executa o comando como se estivesse acessando o atributo porém esta usando o metodo

    @limite.setter
    def limite(self, limite):  # deixar o set mais amigavel com o desenvolvedor
        self.__limite = limite
        # setters
        # executa o comando como se estivesse acessando o atributo porém esta usando o metodo
        # definir primeiro o getter depois o setter

    @property
    def codigo_banco(self):
        return self.__codigo_banco

















