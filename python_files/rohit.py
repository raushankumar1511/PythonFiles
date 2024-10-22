numbers = [5,6,2,6,9]
numbers.append(20)
print(numbers)
print(numbers.index(5))
print(50 in numbers)
print(6 in numbers)
numbers.sort()
print(numbers)

numbers2 =numbers.copy()
numbers.append(10)
print(numbers)