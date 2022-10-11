#Given an array of integers, find two numbers in it such that they can add up to a specific number.
#You may assume there are exactly one solution, you can’t use the same element twice. (Only time-complexity optimized solution gets full grade)
#Example:
#Given [2, 7, 11, 4], Target = 13.
#The answer is 2 and 11.

def solution(list, num):
    hashtable = {}

    for i, a in enumerate(list):
        b = num - a
        if (b in hashtable):
            return hashtable[b],b
        hashtable[a] = b
    else:
        return ('None found')

numbers = [0, 21, 78, 19, 90, 13]
print(solution(numbers, 103))
#print(solution(numbers, 78))
## Using hashtable strategy, we used the for loop only once and reduced the complexity to O(n)
# instead of the usual double "for loops" which result in O(n^2)