salario = float(input("Digite o seu salário: "))

if salario > 1.500:
    print(f"O seu salário atual será de: {(salario*0.10)+salario}")
else:
    print(f"O seu salário atual será de: {(salario*0.15)+salario}")