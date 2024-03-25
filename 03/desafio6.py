def main():
    nome = str(input("Digite o nome completo: "))
    prim = nome.split()
    ult = nome.split()
    print(f"{prim[0]}")
    print(f"{ult[-1]}")
if __name__ == "__main__":
    main()