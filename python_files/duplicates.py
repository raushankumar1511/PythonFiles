numbers = [2,4,5,5,2,65,6,4,78]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
uniques.sort()
print(uniques)
 