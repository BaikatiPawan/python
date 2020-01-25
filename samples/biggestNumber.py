def largestNumber(list):
    maxValue = list[0]
    for num in list:
        if maxValue < num:
            maxValue = num
    return maxValue

print(largestNumber([2,4,92,50,1,70]))
