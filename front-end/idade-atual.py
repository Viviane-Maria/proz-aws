nome = input("Digite seu nome completo: ")

def obterIdade():
    while True:
        try:
            anoNascimento = int(input("Digite o ano de nascimento (entre 1922 e 2022): "))
            if (anoNascimento >= 1922) and (anoNascimento <= 2022): #Verifica se está no intervalo de 1922 até 2022
                idade = 2023 - anoNascimento
                return print(f"Nome: {nome} completou ou completará {idade} anos em 2023.")
            else:
                print("Ano fora do intervalo permitido. Tente novamente.") # Caso o usuário digite um ano fora do intervalo.
        except ValueError:
            print("Valor inválido. Digite um número válido.") # Caso o usuário digite letras em vez de números inteiros.

obterIdade()