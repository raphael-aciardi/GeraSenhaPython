import random

letras = "qwertyuiopasdfghjklçzxcvbnm!@#$%¨&*()1234567890[]:.;"

def CriarSenha(tamanho:int, senha=" "):
    if tamanho <= len(senha):
        return senha
    else:
        numero_aleatorio = random.randint(0, len(letras) - 1)
        return CriarSenha(tamanho,senha + str(letras[numero_aleatorio]))

print(CriarSenha(int(input("Digite a quantidade de caracteres da senha: "))))