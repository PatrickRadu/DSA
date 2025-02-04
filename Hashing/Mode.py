def mode (nums):
    Max=0
    counts={}
    for num in nums:
        if num not in counts:
            counts[num]=0
        else:
            counts[num]+=1
        if counts[num]>Max:
            Max=counts[num]
    return Max

def find_mode(numbers):
    count = {}
    mode = (0, 0)

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        mode = max(mode, (count[x], x))

    return mode[1]