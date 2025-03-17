def insertion_sort(nums, k, result):
    count = 0
    for i in range(1, len(nums)):
        loc = i - 1
        newItem = nums[i]
        while loc >= 0 and newItem < nums[loc]:
            count += 1
            nums[loc+1] = nums[loc]
            if count == k: result = nums[loc]
            loc -= 1
        
        if loc+1 != i:
            count += 1
            nums[loc+1] = newItem
            if count == k: result = nums[loc]
    
    return result

a, k = map(int, input().split(" "))
result = -1
print(insertion_sort(list(map(int, input().split(" "))), k, result))
