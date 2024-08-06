def findGCD(nums):
    nums.sort()
    low = nums[0]
    high = nums[len(nums)-1]
    # print(high,low)
    while (low!=0 and high!=0):
        if(low >= high):
            low = low - high
            # print(low)
        else:
            high = high - low
            # print(high)
    return low or high


nums = [2,5,6,9,10]
# print('Begin')
print(findGCD(nums))