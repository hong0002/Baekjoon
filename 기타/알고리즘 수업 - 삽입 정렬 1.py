def insertion_sort(nums, k):
    count = 0
    for i in range(1, len(nums)):
        loc = i - 1
        newItem = nums[i]
        while loc >= 0 and newItem < nums[loc]:
            count += 1
            nums[loc+1] = nums[loc]
            if count == k:
                return nums[loc]
            loc -= 1
        
        if loc+1 != i:
            count += 1
            nums[loc+1] = newItem
            if count == k:
                return nums[loc]
    
    return -1

a, k = map(int, input().split(" "))
print(insertion_sort(list(map(int, input().split(" "))), k))
