def main():
    n1 = int(input("Digite a idade do nadador:"))

    if n1 < 5:
        print(f"Digite uma idade válida.")
    elif n1 >= 5 and n1 <=7 :
        print(f"Infantil A")
    elif n1 >= 8 and n1 <=11 :
        print(f"Infantil B")
    elif n1 >= 12 and n1 <=13 :
        print(f"Juvenil A")
    elif n1 >= 14 and n1 <=17 :
        print(f"Juvenil B")
    else:
        print("Adultos")

if __name__ == "__main__":
    main()