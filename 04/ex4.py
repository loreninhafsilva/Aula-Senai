from datetime import date

def main():
    n1 = int(input("Digite o seu ano de nascimento:"))
    anoAtual = date.today().year
    if anoAtual-n1 <= 18:
        print(f"Você é maior de idade")
    else:
        print(f"Você é menor de idade")

if __name__ == "__main__":
    main()