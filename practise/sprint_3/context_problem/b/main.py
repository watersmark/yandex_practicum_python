def quicksort(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = (fst + lst) // 2

    while i <= j:
        while nums[i] < nums[pivot]:
            i += 1
        while nums[j] > nums[pivot]:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


mass = [1, 4, 9, 7]
quicksort(mass, 0, len(mass) - 1)
print(mass)