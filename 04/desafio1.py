import random
num = random.randint(0, 5)

palpite = int(input("Tente adivinhar o número que o computador escolheu (entre 0 e 5): "))

if palpite == num:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou! O número escolhido pelo computador foi {num}.")
