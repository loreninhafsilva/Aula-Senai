def main():
    cidade = str(input("Digite o nome de uma cidade: "))
    santo = cidade.upper()
    santo = cidade.split()
    if santo[0] != "Santo" :
        print(f"O nome da cidade não começa com Santo")
    else :
        print(f"O nome da cidade começa com Santo")

if __name__ == "__main__":
    main()