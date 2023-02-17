class Filme:
    def __init__(self,nome, ano, duracao, likes):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        self.likes = likes

class Serie:
    def __init__(self,nome, ano, temporadas,likes):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.likes = likes



vingadores = Filme('Vingadores',2022, 160)
print(vingadores.nome)

invencivel = Serie('invencivel',2022,1)
print(f'Nome:{invencivel.nome}, Ano:{invencivel.ano}, Temporadas:{invencivel.temporadas}')