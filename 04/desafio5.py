def main():
    ano = int(input("Digite um ano para ver se ele é bissexto: "))
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print("O ano digitado é bissexto")
    else:
        print("O ano digitado não é bissexto")
if __name__ == "__main__":
    main()
