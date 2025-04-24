palavra = ('Aprender', 'Programar', 'Linguagem','Python', 'Curso','Gratis', 'Estudar','Praticar', 'Trabalhar','Mercado', 'Programador','Futuro')


for p in palavra:
    print(f"\nNa palavra {p.upper()} temos ",end='')
    for l in p:
        if l.lower() in "aeiou":
            print(l, end=' ')