class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'
    
    
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Filme: {self.nome} - {self.ano} - {self.duracao} min - {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Série: {self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes}'


fantasma_da_opera = Filme('o fantasma da opera', 2014, 150)
loki = Serie ('loki', 2021, 1)
jacobs_ladder = Filme('jacobs ladder', 1972, 170)
mindhunter = Serie('mindhunter', 2016, 2)
fantasma_da_opera.dar_likes()
fantasma_da_opera.dar_likes()
fantasma_da_opera.dar_likes()
loki.dar_likes()
jacobs_ladder.dar_likes()
jacobs_ladder.dar_likes()
jacobs_ladder.dar_likes()
jacobs_ladder.dar_likes()
mindhunter.dar_likes()
mindhunter.dar_likes()

pl = [fantasma_da_opera, mindhunter, jacobs_ladder, loki]
playlist = Playlist("Playlist para 21hrs", pl)

for p in playlist:
    print (p)
