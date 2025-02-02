# You are given a list containing
# n
# n integers. Your task is to count how many ways one can split the list into two parts so that both parts have the same total sum of elements.
#
# Consider the following example list:
#
# Position	0	1	2	3	4	5	6	7
# Number	1	-1	1	-1	1	-1	1	-1
# Here the number of ways is 3. We can split the list between positions
# 1 and 2, between positions 3 and 4, and between positions 5 and 6.

def counts_splits_Bf(numbers):
    n=len(numbers)
    result=0
    for i in range(n-1):
        leftSum=sum(numbers[0:i+1])
        rightSum=sum(numbers[i+1:])
        if leftSum==rightSum:
            result+=1
    return result

def counts_splits_BF2(numbers):
    n=len(numbers)
    result=0
    left_sum=0
    for i in range(n-1):
        left_sum+=numbers[i]
        right_sum=sum(numbers[i+1:])
        if left_sum==right_sum:
            result+=1
    return result

def count_splits(numbers):
    n=len(numbers)
    result=0
    left_sum=0
    right_sum=0
    total_sum=sum(numbers)
    for i in range(n-1):
        left_sum+=numbers[i]
        right_sum=total_sum-left_sum
        if left_sum==right_sum:
            result+=1
    return result