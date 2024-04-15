import re
def main():
    valor_emprestimo = float(input("Digite o valor do empréstimo: "))
    salario = float(input("Digite o salário líquido do solicitante: "))
    meses_pagamento = int(input("Digite a quantidade de meses para pagamento: "))

    nome = input("Digite o nome completo: ")
    nome = nome.title()

    continuar = True  
    while continuar:
        cpf = input("Digite o CPF: ")
        cpf = re.sub(r'\D', '', cpf)  
        if len(cpf) != 11:
            print("CPF inválido. Digite um CPF com 11 dígitos.")
        else:
         continuar = False

    continuar2 = True  
    while continuar2:
        telefone = input("Digite o número de telefone para contato: ")
        telefone = re.sub(r'\D', '', telefone)
        if len(telefone) != 11:
            print("Telefone inválido, digite um número com 11 dígitos")
        else:
         continuar2 = False

    endereco = input("Digite o seu endereço: ")

    continuar3 = True  
    while continuar3:
        cep = input("Digite o CEP: ")
        cep = re.sub(r'\D', '', cep)
        if len(cep) != 8:
            print("CEP inválido, digite um CEP com 8 dígitos")
        else:
         continuar3 = False

    continuar4 = True  
    while continuar4:
        email = input("Digite o e-mail: ")
        if not email.endswith('@gmail.com'):
            print("Email inválido, ele precisa ser obrigatoriamente um endereço do Gmail")
            email.lower()
        else:
            continuar4 = False
            email.lower()

    prestacao = valor_emprestimo / meses_pagamento

    print(f"Nome: {nome}\nCPF: {cpf}\nTelefone: {telefone}\nEndereço: {endereco}\nCEP: {cep}\nEmail: {email}\n")
    if prestacao <= salario * 0.3:
        print("Empréstimo aprovado!")
        print(f"O valor da prestação é: {prestacao}")
    else:
        print(f"Empréstimo negado")


if __name__ == "__main__":
    main()