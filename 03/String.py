def main():
    frase = str(input("Digite uma sequência: "))
    apartirFinal = frase[5:] # Mostra a partir do final
    apartirComeco = frase[:5] # Mostra a partir do começo
    intervalo = frase[5:8] # Mostra o intervalo 
    intervaloIntercalado = frase[5:8:2] # Mostra o intervalo indo de 2 em 2
    doisEmDois = frase[::2] # Mostra a frase inteira indo de 2 em 2
    posicao = frase[5] # Mostra só o que está nessa posição
    tudo = frase[:] # Mostra a frase inteira
    tamanhoFrase = len(frase) # Mostra a quantidade de caracteres da frase
    repeticao = frase.count("3") # Mostra quantas vezes esse caractare aparece na frase
    posicaoPalavra = frase.find("casa") # Mostra a posição onde a palavra aparece
    aparece = "casa" in frase # Verifica se existe na frase
    maiusculo = frase.upper() # Transforma em maiusculo
    minusculo = frase.lower() # Transforma em minúsculo
    capitalize = frase.capitalize() # Transforma só a primeira letra em maiúsculo
    titulo = frase.title() # A primeira letra de cada palavra fica maiúscula
    troca = frase.replace("Capeta", "Jesus") # Troca
    print(f"O quarto caractere é: {posicao}")
    print(f"O tamanho da sentença é: {tamanhoFrase}")
    print(f"O número 3 aparece: {repeticao} vezes na sentença")
    print(f"A palavra casa aparece na posição {posicaoPalavra}")
    print(f"A palavra casa aparece na frase: {aparece}")
    print(f"A frase maiúscula é: {maiusculo}")
    print(f"A frase minúscula é: {minusculo}")
    print(f"A frase com a primeira letra minúscula fica: {capitalize}")
    print(f"A frase transformada em título: {titulo}")
    print(f"{troca}")

if __name__ == "__main__":
    main()