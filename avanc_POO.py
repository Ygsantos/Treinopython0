class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title() #remover o __ duplo e deixar o unico para evitar
        self.ano = ano             #erro ao chamar a funcao relacionada ao atributo.
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self): #Representa o objeto daquela classe textualmente, nao sera necessario imprimir com o if.
        return f'Nome: {self.nome} Likes: {self.likes}'
class Filme(Programa): #Classe agora tem uma classe mae, a mesma herdou os metodos de Programa.
                       #Passar como parametro a classe mae.
                       #python suporta heranca de mais de uma classe.
    def __init__(self,nome, ano, duracao):
        super().__init__(nome,ano)#Chamar a classe mae atraves do inicializador.
        self.duracao = duracao    # reduziu a quantidade de codigo repetitivo com a heranca.

    def __str__(self): #Representa o objeto daquela classe textualmente, nao sera necessario imprimir com o if.
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa): #Classe agora tem uma classe mae, a mesma herdou os metodos de Programa.
                       #Passar como parametro a classe mae.
                       # python suporta heranca de mais de uma classe.
    def __init__(self,nome, ano, temporadas):
        super().__init__(nome,ano) #Chamar a classe mae atraves do inicializador. ''Super' chama o metodo da classe mae.
        self.temporadas = temporadas # reduziu a quantidade de codigo repetitivo com a heranca.

    def __str__(self): #Representa o objeto daquela classe textualmente, nao sera necessario imprimir com o if.
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist(): #Criando classe playlist
    def __init__(self, nome, programas): #Recebe como parametro o nome da playlist e os programas da playlist.
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist.listagem:
    print(programa)

print(f'Tamanho: {len(minha_playlist.listagem)}')


#Polimorfismo, como sao do mesmo supertipo consgue acessar as duas.

#hasatrr(parametros, item a procurar)