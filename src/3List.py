nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(nums))
print(nums)
print(nums[2])
print(nums[9])
print(nums[:4])
print(nums[4:])
print(nums[-1])

name = ['manju', 'mahendra', 'ravi']
print(name)
print(name[2])

values = [9, 5, 'manju', 25]
print(values[2])

mil = [nums, name]
print(mil)
# insert at the end
nums.append(45)
print(nums)
# insert by index
nums.insert(2, 11)
print(nums)
# remove the element
nums.remove(11)
print(nums)
# remove by index
nums.pop(10)
print(nums)

nums.append(45)
print(nums)
del nums[10]
print(nums)
nums.extend([11, 12, 13, 14])
print(nums)

print(min(nums))
print(max(nums))