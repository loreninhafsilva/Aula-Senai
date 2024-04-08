distancia = float(input("Digite a distância da sua viagem em km: "))

if distancia < 200:
    print(f"O preço da sua passagem é: {distancia*0.50}")
else:
    print(f"O preço da sua passagem é: {distancia*0.45}")
