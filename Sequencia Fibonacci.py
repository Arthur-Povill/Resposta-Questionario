def fibonacci_sequence(number):
    # Inicializando os primeiros termos da sequência
    Termo1 = 0
    Termo2 = 1

    # Lista para armazenar a sequência de Fibonacci
    fibonacci_list = [Termo1, Termo2]

    # Gera a sequência até que o próximo termo seja maior ou igual ao número informado
    while Termo2 < number:
        Termo1, Termo2 = Termo2, Termo1 + Termo2
        fibonacci_list.append(Termo2)

    # Verifica se o número pertence à sequência
    if number in fibonacci_list:
        return f'O número {number} faz parte da sequência de Fibonacci.'
    else:
        return f'O número {number} não faz parte da sequência de Fibonacci.'


# Define o valor diretamente no código
Valor = 21  # Aqui você pode substituir pelo número desejado

# Chama a função e imprimir o resultado
print(fibonacci_sequence(Valor))
