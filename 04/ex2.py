def main():
    n1 = int(input("Digite um número:"))
    n2 = int(input("Digite outro número:"))
    if n1 > n2:
        print(f"O número {n1} é o maior e {n2} é o menor")
    else:
        print(f"O número {n2} é o maior e {n1} é o menor")

if __name__ == "__main__":
    main()