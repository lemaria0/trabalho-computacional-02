def ord_cresc_string(texto):
    letras = []
    for c in texto:
        if c != ' ':
            letras.append(c)

    n = len(letras)
    for i in range(n):
        for j in range(0, n - i - 1):
            if letras[j] > letras[j + 1]:
                letras[j], letras[j + 1] = letras[j + 1], letras[j]

    resultado = ''
    for letra in letras:
        resultado += letra

    print("String ordenada crescentemente:", resultado)

texto = input("Digite uma string: ")
ord_cresc_string(texto)