def spy_game(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+3] == [0, 0, 7]:
            return True

    return False

print(spy_game([1, 5, 6, 0, 0, 7, 34, 12, 36]))            