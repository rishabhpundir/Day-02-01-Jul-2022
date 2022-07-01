

a=['flowing','flow','flame','fldo']

letters = []
counter=1
common_letters = []

for y in a:
    for i in y:
        letters.append(i)

for i in range(0, len(letters)):
    counter=1
    for j in range(i+1, len(letters)):
        if letters[i] == letters[j]:
            counter+=1

    if counter>=len(a) and letters[i] not in common_letters:
        common_letters.append(letters[i])

print(common_letters)





