import math
num = int(input("Digite um número: "))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tg = math.tan(math.radians(num))
print(f"\nO seno do ângulo de {num}° é {sen:.2f}")
print(f"O cosseno do ângulo de {num}° é {cos:.2f}")
print(f"A tangente do ângulo de {num}° é {tg:.2f}")