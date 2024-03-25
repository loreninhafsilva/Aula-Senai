def main():
    nome = str(input("Digite o nome completo: "))
    prim = nome.split()
    print(f"{nome.upper()}")
    print(f"{nome.lower()}")
    print(f"{len(nome.strip())}")
    print(f"{len(prim[0])}")

if __name__ == "__main__":
    main()