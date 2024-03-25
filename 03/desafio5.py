def main():
    frase = str(input("Escreva uma frase: "))
    frase = frase.upper()
    print(f"A letra A aparece {frase.count("A")}")
    print(f"A letra A aparece pela primeira vez na {frase.find("A")}° posição ")
    print(f"A letra A aparece pela primeira vez na {frase.rfind("A")}° posição ")
if __name__ == "__main__":
    main()