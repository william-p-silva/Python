from rich import print
from rich.panel import Panel
from time import sleep

class Livro():

    def __init__(self, title, pag):
        self.title = title
        self.pag = pag
        self.pag_atual = 1
        print(f":open_book: Você acabou de abrir o livro {self.title}")


    def passar_paginas(self, qnt):
        if self.pag_atual == 1:
            print("Você está na primeira pagina")
            sleep(0.5)
        for c in range(qnt):
            sleep(0.3)
            if self.pag_atual == self.pag: 
                self.pag_atual += 1
                print(f"Última página {self.pag_atual - 1}")
                continue
            
            self.pag_atual += 1
            if self.pag_atual > self.pag: return f"[red]Você já esta na última página {self.pag}, e não pode mais avancar[/]"

            print(f"{self.pag_atual} > ", end='')
        if self.pag_atual > self.pag: return f"[red]Você já esta na última página {self.pag}, e não pode mais avancar[/]"
        return f'[blue]Você avançou[/] {qnt} paginas e está na [yellow]{self.pag_atual} páginas[/]'
    



livro1 = Livro("Pequeno Principe", 20)
print(livro1.passar_paginas(10))
print(livro1.passar_paginas(9))
print(livro1.passar_paginas(1))

