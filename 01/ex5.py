def main():
    valor = int(input("Digite o valor: "))
    taxa = int(input("Digite a taxa: "))
    tempo = int(input("Digite o tempo: "))

    prestacao = valor + (valor*(taxa/100)*tempo)

    print(f"O valor da prestação é {prestacao}")

if __name__ == "__main__":
    main()