from art import logo

print(logo)
alfabeto = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "
]
palavraFinal = ""
palavraOriginal = ""
palavra = input("Digite a palavra a ser criptografada: ").lower()
chave = int(input("Digite a chave: "))
escolha = int(
    input(
        "Digite (1) para criptografar ou \n(2) para descriptografar a palavra "
    ))
#criptografia
if (escolha == 1):
    for nr in range(len(palavra)):
        indexLetra = (alfabeto.index(palavra[nr]) + chave) % len(alfabeto)
        palavraFinal += alfabeto[indexLetra]

    print(f"Frase criptografada :{palavraFinal}")

#descriptografia
if (escolha == 2):
    for nr in range(len(palavra)):
        indexOriginal = (alfabeto.index(palavra[nr]) -
                         chave) % len(alfabeto)
        palavraOriginal += alfabeto[indexOriginal]
    print('\n')    
    print(f"Frase descriptografada: {palavraOriginal}")

print("Fim do programa.")
