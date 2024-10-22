numbers=[1,3,5,6,2,3,5,5 ,12,3,4,5,6,6]
#numbers2= numbers.copy()
#print(numbers)
#print(numbers2)
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

