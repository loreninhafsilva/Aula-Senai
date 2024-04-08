altura =  float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))
comp = float(input("Digite o comprimento: "))
consumo = float(input("Digite o consumo médio diário (litros/dia): "))

autonomia = (altura*largura*comp)/consumo

print(f"a capacidade total do reservatório é: {altura*largura*comp}")
print(f"A autonomia do reservatório em dias é: {autonomia}")

if autonomia < 2:
    print("Consumo elevado")
elif autonomia >= 2 and autonomia <= 7:
    print("Consumo moderado")
else:
    print("Consumo reduzido")
