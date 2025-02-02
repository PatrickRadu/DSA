
#indexing
numbers= [ 4,3,7,3,2]
print(numbers[2])
numbers[2]=5
print(numbers[2])

#Size
numbers=[4,3,7,3,2]
print(len(numbers))

numbers= [ 4,3,7,3,2]
print( 3 in numbers)
print(numbers.index(3))
print(numbers.count(3))

#Adding
numbers=[1,2,3,4]
numbers.append(5)
print(numbers)
numbers.insert(1,6)
print(numbers)

#Removing
numbers = [1, 2, 3, 4, 5, 6]

numbers.pop()
print(numbers)

numbers.pop(1)
print(numbers)

#Shallow copy
a=[1,2,3,4]
b=a
a.append(5)
print(a,b)

#Deep copy
a=[1,2,3,4]
b=a.copy()
a.append(5)
print(a,b)

def double(numbers):
    result = numbers
    for i in range(len(result)):
        result[i] *= 2
    return result

numbers = [1, 2, 3, 4]
print(double(numbers)) # [2, 4, 6, 8]
print(numbers) # [2, 4, 6, 8]

def double(numbers):
    result = numbers.copy()
    for i in range(len(result)):
        result[i] *= 2
    return result

numbers = [1, 2, 3, 4]
print(double(numbers)) # [2, 4, 6, 8]
print(numbers) # [1, 2, 3, 4]

#Slice
numbers=[1,2,3,4,5,6,7,8]
print(numbers[2:6])


#EQUIVALENT
result=numbers.copy()
result=numbers[:]

#Concat
first=[1,2,3,4]
second=[5,6,7,8]
print(first+second)