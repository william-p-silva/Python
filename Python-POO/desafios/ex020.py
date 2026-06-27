from rich.panel import Panel 
from rich import print

class Games():
    
    def __init__(self, nome, nick_name):
        self.nome = nome
        self.nick = nick_name
        self.favoritos = list()
        
    def add_favorito(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)
        
    def ficha(self):
        conteudo = f"[black]Nome real:[/] [bold black on blue] {self.nome} [/]"
        conteudo += "\nJogos favoritos: "
        for enum, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        return Panel(conteudo, title=f" Jogador<{self.nick}> ", style="green")
        
jg = Games("william", "Pajé")

jg.add_favorito("God of War")
jg.add_favorito("Rockt League")
print(jg.ficha())