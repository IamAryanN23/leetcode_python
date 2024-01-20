def productExceptSelf(nums: list[int]) -> list[int]:
    leng = len(nums)
    newnum = [1] * leng
    i=0
    j=0
    for i in range (leng):
        for j in range (leng):
            if i != j:
                newnum[i] *= nums[j]
    return newnum

print(productExceptSelf([1,2,3,4]))