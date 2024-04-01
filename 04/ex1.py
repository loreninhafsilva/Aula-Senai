def main():
    media = float(input("Digite a média do aluno:"))
    if media < 6:
        print ("Reprovado")
    else:
        print("Recuperação")
if __name__ == "__main__":
    main()