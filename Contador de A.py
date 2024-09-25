def contar_letra_a(texto):
    # Converte o texto para minúsculas para facilitar a contagem
    texto_lower = texto.lower()

    # Conta a ocorrência da letra 'a'
    quantidade_a = texto_lower.count('a')

    # Verifica se a letra 'a' existe e retornar o resultado
    if quantidade_a > 0:
        return f"A letra 'a' aparece {quantidade_a} vez(es) na string."
    else:
        return "A letra 'a' não está presente na string."


# Entrada do usuário
texto_usuario = input("Digite uma string: ")

# Chama a função e imprimir o resultado
print(contar_letra_a(texto_usuario))
