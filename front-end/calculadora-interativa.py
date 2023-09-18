import time # Importa o módulo time para usar a função time.sleep

def calculadora(num1, num2, operacao):
    if operacao == 1: 
        return num1 + num2
    elif operacao == 2: 
        return num1 - num2
    elif operacao == 3: 
        return num1 * num2
    elif operacao == 4: 
        if num2 != 0:  # Verifica se o divisor é diferente de zero, já que não existe divisão por zero.
            return num1 / num2
        else:
            return "Não é possível dividir por zero"
    else:
        return 0

# Condição para o While     
continua = True   

while (continua == True):
    print("Opções:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    operacao = int(input("Escolha uma opção: "))

    if (operacao < 0 or operacao > 4):
        print("Essa opção não existe")
        # Adiciona um delay de 1,5s para aparecer as opções novamente, com esse tempinho o usuário consegue ler o print
        time.sleep(1.5)
    elif(operacao == 0):
        print("Saindo da calculadora...")
        continua = False
    else:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calculadora(num1, num2, operacao)
        """ Verificação do tipo de retorno: Quando precisar lidar com diferentes comportamentos ou mensagens de erro dependendo do tipo de resultado """
        if type(resultado) == str:
            print(resultado)
        else:
            print("Resultado:", resultado)
        # Adiciona um delay de 1,5s para aparecer as opções novamente, com esse tempinho o usuário consegue ler o resultado    
        time.sleep(2)