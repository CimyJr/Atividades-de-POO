"""Fazer uma sequencia de impressão onde sejam mostras as representações  decimal, octal, hexadecimal dos valores inteiros de 0 a 225 (que são os valores que um byte pode representar).
Verificar o contéudo dos especificadores de representação no contexto do comando print.
Cria para cada representação uma função especifica (printDecimal, printOctal, printHexadecimal, printBinario).
Incluir no código uma funcionalidade imprimirTabela() que executar um laço para imprimir cada linha
do relatório.
Layout da saída:
Decimal  Octal  Hexadecimal    Binario
------------- --------- --------------------- -----------------
  999      XXXX       XXXX          99999999
 
Código persistido em um repositório do GitHub."""


def printdec(valor):
    print("{}            ".format(valor), end=" ")


def printoct(valor):
    print("{:9}".format(oct(valor)), end=" ")


def printhex(valor):
    print("{:21}".format(hex(valor)), end=" ")


def printbin(valor):
    print("{:17}".format(bin(valor)), end=" ")


print("{}       {}     {}            {}".format("Decimal", "Octal", "Hexdecimal", "Binario"))
print("------------- --------- --------------------- -----------------")

numero = 0
while numero < 225:
    printdec(numero)
    printoct(numero)
    printhex(numero)
    printbin(numero)
    print("\n")
    numero += 1
