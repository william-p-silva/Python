

contador = 0
s = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s += c
        contador += 1
print("A somas de todos os {} valores solicitados é {}".format(contador,s))
    
    
    