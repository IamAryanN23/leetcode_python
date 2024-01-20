def moveZeroes(nums: list[int]) -> None:
    idx2 = 0
    for idx1 in range(len(nums)):
        if nums[idx1] != 0:
            nums[idx2] = nums[idx1]
            idx2 += 1
    for remainIdx in range(idx2, len(nums)) :
        nums[remainIdx] = 0
    return nums


print (moveZeroes([0,1,0,3,12]))