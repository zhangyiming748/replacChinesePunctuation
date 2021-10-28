# 编写程序,利用Python中的方法和函数提取出给定列表5,8,-7,4,6,2,-3,0中的最大？
def maxNumber(nums):
    return max(nums)


def maxNumberWithOutFunc(nums):
    maxNumber = nums[0]
    for n in nums:
        if n > maxNumber:
            maxNumber = n
    return maxNumber


if __name__ == '__main__':
    nums = [5, 8, -7, 4, 6, 2, -3, 0]
    print("max is %d" % maxNumber(nums))
    print("max is %d" % maxNumberWithOutFunc(nums))
