def valid(nums):
    if nums is None or len(nums) < 2:
        return 0
    nums.sort()
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if isValid(nums[i], nums[j], nums[k]):
                    res += 1
    return res

def optimized(nums):
    if nums is None or len(nums) < 2:
        return 0
    nums.sort()
    n = len(nums)
    i = n - 1
    res = 0
    while i > 1:
        left, right = 0, i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                res += 1
                right -= 1
            else:
                left += 1
    return res

def isValid(a, b, c):
    return a + b > c