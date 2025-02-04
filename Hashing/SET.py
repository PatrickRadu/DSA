numbers=set()
numbers.add(1)
numbers.add(2)
numbers.add(3)
print(numbers)

numbers=set([1,2,3])
print(numbers)

print(3 in numbers)
print(4 in numbers)

numbers.remove(2)
print(numbers)

#O(1)