from random import randint


randon5 = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))


for i in randon5:
    print(i, end='  ')
   
print(f"\nO maior número foi {max(randon5)}")
print(f"O menor número foi {min(randon5)}")