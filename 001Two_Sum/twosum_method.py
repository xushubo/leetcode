import operator

def twoSum(nums, target):
    num_list = [(i, nums[i]) for i in range(len(nums))]
    num_list.sort(key=operator.itemgetter(1))
    n = 0
    m = len(nums)-1
    while True:
        if n == m:
            break
        num_sum = num_list[n][1] + num_list[m][1]
        if num_sum == target:
            break
        elif num_sum > target:
            m-=1
        else:
            n+=1
    return list(sorted((num_list[n][0], num_list[m][0])))

print(twoSum([1, 2 ,3 ,4], 6))