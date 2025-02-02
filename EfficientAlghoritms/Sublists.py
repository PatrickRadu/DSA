# You are given a list containing
# n integers. How many ways can we choose a sublist that contains exactly two distinct integers?

def count_lists(numbers):
    n=len(numbers)
    a=b=-1
    result=0
    for i in range(1,n):
        if numbers[i]!=numbers[i-1]:
            if numbers[i]!=numbers[a]:
                b=a
            a=i-1
        result+=a-b
    return result