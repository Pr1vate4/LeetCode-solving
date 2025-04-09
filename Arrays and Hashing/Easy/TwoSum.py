#  [2,7,11,15]
# короче я не знал как нормально принять массив, по этому изобрел свой способ
nums = str(input())
nums2 = nums.replace("[" , ",")
nums2 = nums2.replace("]" , ",")
nums3 = nums2.split(",")
nums3.remove("")
nums3.remove("")
nums = nums3
target = int(input())
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[j] == target - int(nums[i]):
            print([i, j])
# for i in range(len(nums)):
#     if (nums[0] == nums[-1]) and (int(nums[0]) + int(nums[-1])) == target:
#         x = [0, len(nums)]
#         print(x)
#         break
            
#     if int(nums[i - 1]) + int(nums[i]) == target:
#         x = [i - 1, i]
#         print(x)
#     i += 1

    # def twoSum(nums = str(input()), target =  int(input())):
#     nums2 = nums.replace("[" , ",")
#     nums2 = nums2.replace("]" , ",")
#     nums3 = nums2.split(",")
#     nums3.remove("")
#     nums3.remove("")
#     nums = nums3
#     for i in range(len(nums)):
#         if int(nums[i - 1]) + int(nums[i]) == target:
#             x = [i - 1, i]
#             return x
#         i += 1