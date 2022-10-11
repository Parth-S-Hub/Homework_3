class Solution:
    def isanagram(self, a, b):

        if sorted(a) == sorted(b):
            return True
        else:
            return False

if __name__ == '__main__':
    a = "ram"
    b = "arm"
    if (Solution().isanagram(a, b)):
        print("True")
    else:
        print("False")
##Time complexity is O(NlogN) since we are usuing sorted