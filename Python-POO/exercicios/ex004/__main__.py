from rich import inspect
import Pessoa
from Professor import Professor
import Aluno
import Funcionario

def main():  
    prof = Professor("joão", 20, "Banco de dados", 3)

    inspect(prof)

if __name__ == "__main__":
    main()