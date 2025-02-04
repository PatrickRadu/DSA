#You are given a list of numbers. How many distinct numbers does it contain?


def countDistinct(numbers):
    numSet=set(numbers)
    return len(numSet)