
def listSums(nums,x):
    count={0:1}
    prefix_sum=0
    result=0
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        if prefix_sum - x in count:
            result+=count[prefix_sum-x]
        if prefix_sum not in count:
            count[prefix_sum]=0
        count[prefix_sum]+=1
    return result