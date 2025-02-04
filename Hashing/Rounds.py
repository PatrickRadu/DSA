def count_rounds(numbers):
    n = len(numbers)

    rounds = 1
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1

    return rounds
def rounds(nums):
    numsPos={}
    for i in range(len(nums)):
        numsPos[nums]=i
    rounds=1
    for i in range(1,len(nums)):
        if  numsPos[i+1]<numsPos[i]:
            rounds+=1
    return rounds
