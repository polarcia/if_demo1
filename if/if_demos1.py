# testa uma palavra introduzida pelo o utilizador
# se for "spathiphyllum" escreve "Yes - Spathiphyllum is the best plant ever!"
# se nao for "spathiphyllum" esvreve "No, I want a big Spathiphyllum!"
# sendo escreve "Spathiphyllum! Not [input]!"

nome = input("introduza um nome de flor: ")

if nome == "Spathiphyllum" : print("Yes - Spathiphyllum is the best plant ever!")
elif nome == "spathiphyllum": 
    print("No, I want a big Spathiphyllum!")
else:
        print("Spathiphyllum! Not " , nome, "!", sep= "")