# Código do while em pseudocódigo comentado porque não tem em Python. Imprime em ordem decrescente:
""" andar = 20

ENQUANTO andar >= 1 FAÇA
    SE andar ≠ 13 ENTÃO
        IMPRIMIR andar
    FIM SE
    andar = andar - 1
FIM ENQUANTO """

# Agora usando os laços de repetição da Python, também imprime em ordem decrescente:

# Loop While
andar = 20

while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1

#  Loop For
for andar in range(20, 0, -1):
    if andar != 13:
        print(andar)
