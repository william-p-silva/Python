from rich.panel import Panel
from rich import print
import os
import time

class Tv():
    def __init__(self):
        self.canais = 5
        self.volume = 5
        self.canal_atual = 1
        self.ligada = False
        self.volume_atual = 3
        
        
    def tela_tv(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        time.sleep(0.1)

        if self.ligada:
            conteudo = f"CANAL =  "
            for c in range(1, self.canais + 1):
                if self.canal_atual == c:
                    conteudo += f"[blue on yellow] {c} [/]"
                else: 
                    conteudo += f" {c} "
            
            conteudo += "\nVOLUME = "
            for f in range(self.volume_atual):
                conteudo += "[blue on blue]   [/]"
                
            for v in range(self.volume - self.volume_atual):
                conteudo += "[blue on white]   [/]"
                
        else:            
            conteudo = "[red]Tv desligada[/]"
            
        painel = Panel(conteudo, title="[ TV ]", width=30)
        print(painel)
    
    
    def ligar_tv(self):
        self.ligada = True
        
        
    def desligar_tv(self):
        self.ligada = False
        

    def controle(self):
        self.tela_tv()
        if self.ligada:
            escolha = str(input("( < CH1 >   - VOL2 + ): "))
            if escolha == "@":
                self.desligar_tv()
            if escolha == "-1":
                return -1
            self.acao(escolha)
        else:
            escolha = str(input("Ligar TV? [@]: "))

            if escolha == "@":
                self.ligar_tv()
            if escolha == "-1":
                return -1
            
        
    def acao(self, escolha):
        match escolha.lower().strip():
            case "<":
                
                if self.canal_atual <= 1:
                    self.canal_atual = self.canais
                elif self.canal_atual > self.canais:
                    self.canal_atual = 1
                else:
                    self.canal_atual -= 1
                    
            case ">":
                
                if self.canal_atual <= 0:
                    self.canal_atual = self.canais
                elif self.canal_atual == self.canais:
                    self.canal_atual = 1
                else:
                    self.canal_atual += 1
                    
            case "+":
                if self.volume_atual >= self.volume:
                    self.volume_atual = self.volume
                else:
                    self.volume_atual += 1
                    
            case "-":
                
                if self.volume_atual <= 1:
                    self.volume_atual = 1
                else:
                    self.volume_atual -= 1
                
            case _:
                return 0
    
canal = Tv()

while True:
    result = canal.controle()
    if result == -1:
        break