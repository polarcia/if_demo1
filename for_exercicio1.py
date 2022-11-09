user_word= input("escreve uma palavra: ")
print(user_word)
user_word= user_word.upper()
print(user_word)

for letra in user_word:
    if letra == "A":
        continue
    print(letra)

