class Filme:
    def __init__(self,nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self,nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.likes+=1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome.title()




vingadores = Filme('Vingadores',2022, 160)
print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, duracao: {vingadores.duracao}, Likes: {vingadores.likes}')




invencivel = Serie('invencivel',2022,1)
print(f'Nome:{invencivel.nome}, Ano:{invencivel.ano}, Temporadas:{invencivel.temporadas}, Likes: {invencivel.likes}')
