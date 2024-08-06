def gcd(small,large):
    if small==0:
        return large
    ans = large%small
    if ans > small:
        return gcd(small,ans)
    else:
        return gcd(ans,small)

class Solution:
    def findGCD(nums):
        nums.sort()
        small = nums[0]
        large = nums[len(nums)-1]
        return gcd(small,large)
            