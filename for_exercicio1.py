word_without_vowels = ""

user_word= input("escreve uma palavra: ")
print(user_word)
user_word= user_word.upper()
print(user_word)

for letra in user_word:
    if letra == "A": continue
    elif letra == "R": continue
    elif letra == "O": continue
    elif letra == "G": continue
    word_without_vowels += letra 
    
    print(word_without_vowels)
