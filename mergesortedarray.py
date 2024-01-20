def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    return nums1[:m] + nums2[:n]
    
def alsomerge(nums1: list[int], m: int, nums2: list[int], n: int) :
    for j in range(n):
        nums1[m+j] = nums2[j]
    nums1.sort()
    return nums1
    
    
#print(merge([1,2,3,0,0,0],3,[2,5,6],3))
print(alsomerge([1,2,3,0,0,0],3,[2,5,6],3))