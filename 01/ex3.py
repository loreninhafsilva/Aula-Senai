def main():
    # Solicita ao usuário que insira um número inteiro
    numero = int(input("Digite um número inteiro: "))
    
    # Calcula o sucessor e o antecessor do número
    sucessor = numero + 1
    antecessor = numero - 1
    
    # Imprime o sucessor e o antecessor na tela
    print(f"O sucessor de {numero} é {sucessor}.")
    print(f"O antecessor de {numero} é {antecessor}.")

if __name__ == "__main__":
    main()
