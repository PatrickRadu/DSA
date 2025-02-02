# You are given a bit string consisting of the characters 0 and 1. How many ways can you select two positions in the bit string so that the left position contains the bit 0 and the right position contains the bit 1?
#
# Consider the following situation:
#
# Position	0	1	2	3	4	5	6	7
# Bit	    0	1	0	0	1	0	1	1
# Here there are 12 such pairs of positions.

def count_ways_brute(bits):
    n=len(bits)
    result=0
    for i in range(n):
        for j in range(i+1,n):
            if bits[i]=='0' and bits[j]=='1':
                result+=1
    return result
#O(N^2)
def count_ways(bits):
    n=len(bits)
    result=0
    zeros=0
    for i in range(len(bits)):
        if bits[i]=='0':
            zeros+=1
        if bits[i]=='1':
            result+=zeros
    return result
#O(N)