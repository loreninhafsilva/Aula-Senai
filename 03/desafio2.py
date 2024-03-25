def main():
    numero = int(input("Digite um númnero entre 0 e 9999: "))
    print(f"Unidade: {numero % 10}")
    print(f"Dezena: {(numero // 10) % 10}")
    print(f"Centena: {(numero // 100) % 10}")
    print(f"Milhar: {(numero // 1000) % 10}")

if __name__ == "__main__":
    main()