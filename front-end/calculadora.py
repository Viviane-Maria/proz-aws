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

resultado = calculadora(7, 7, 3)

""" Verificação do tipo de retorno: Quando precisar lidar com diferentes comportamentos ou mensagens de erro dependendo do tipo de resultado """
if type(resultado) == str:
    print(resultado)
else:
    print("Resultado:", resultado)
