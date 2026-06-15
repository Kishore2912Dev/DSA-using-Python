def find_missing_number(nums):
  n = len(nums)
  xor_sum = n+1
  for i in range(n):
    xor_sum ^= (i+1) ^ nums[i]
  return xor_sum
nums = [1,2,4,5]
result = find_missing_number(nums)
print("The missing number is:",result)