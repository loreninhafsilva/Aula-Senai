velocidade = float(input("Digite a velocidade do seu carro: "))

if velocidade > 80:
    print(f"Você foi multado. Sua multa é de: {(velocidade-80)*7}")