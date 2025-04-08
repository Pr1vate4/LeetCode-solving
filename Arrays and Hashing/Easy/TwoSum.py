#[2,7,11,15] не дорешал, короче у меян идея создать свой алгоритм,где дается массив, а я его преобразую в свой массив
nums = []

dumb_nums = list(input())
for i in range(len(dumb_nums)):
    if dumb_nums[i - 1] == int:
        nums.append


print(type(nums), nums)
target = int(input())

for i in range(len(nums)):
    if nums[i - 1] + nums[i] == target:
        x = [i - 1, i]
        print(x)
    i += 1