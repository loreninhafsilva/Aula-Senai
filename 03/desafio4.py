def main():
    nome = str(input("Digite seu nome: "))
    nome = nome.upper()
    silva = "SILVA" in nome
    if silva == False :
        print(f"O nome não tem Silva")
    else :
        print(f"O nome tem Silva")

if __name__ == "__main__":
    main()