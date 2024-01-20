def removeElement(nums: list[int], val: int) -> int:
    count = 0
    for number in nums:
        if number == val:
            count += 1
    for i in range (count):
        nums.remove(val)
    return nums

print(removeElement([3,2,2,3],3))