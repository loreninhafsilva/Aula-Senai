def main():
    media = float(input("Digite a média do aluno:"))
    if media > 7:
        print("Aprovado")
    elif media < 5:
        print ("Reprovado")
    else:
        print("Recuperação")

if __name__ == "__main__":
    main()