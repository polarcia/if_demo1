# step 1
beatles = []
print(beatles)

# step 2
beatles.append( "John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for members in range(2):
    beatles.append(input("escolhe quem adicionar" ))
    break
print(beatles)

del beatles[-1]
del beatles[-1]
print (beatles) 

beatles.insert(0, "Ringo Starr")
print(beatles)