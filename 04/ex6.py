def main():
    n1 = int(input("Digite os gols do primeiro time:"))
    n2 = int(input("Digite os gols do segundo time:"))

    if n1 == n2:
        print(f"Foi um empate")
    elif n1 > n2:
        print(f"O primeiro time ganhou")
    else:
        print(f"O segundo time ganhou")

if __name__ == "__main__":
    main()