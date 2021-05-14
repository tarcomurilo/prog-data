#Este pequeno projeto faz parte do estudo de python

#função de validação da entrada
def validarEntrada(valor):
    saida = 0
    if len(valor) > 8:
        print("O número de caracteres é maior que 8. Finalizando.")
        saida = -1
        return saida

    for char in valor:
        if (char != "0" and char != "1"):
            print("Foi utilizado um caractere errado. Finalizando.")
            saida = -2
            return saida

    saida = valor
    return str(saida)

#função de conversão
def converterValor(valor):
    valor = valor[::-1]

    saida = 0
    for indice, numero in enumerate(valor):
        if numero == "1":
            saida = saida + pow(2, indice)
        else:
            pass

    return saida

print(f"Conversor de Binário para Decimal")
print(f"O valor deve ter entre 1 e 8 caracteres")
print(f"Utilize apenas 0 ou 1")

valorEntrada = input("Digite o número: ")
valorValido = validarEntrada(valorEntrada)

if int(valorValido) >= 0:
    print(f"O valor convertido é : {converterValor(valorValido)}")
else:
    exit(1)
