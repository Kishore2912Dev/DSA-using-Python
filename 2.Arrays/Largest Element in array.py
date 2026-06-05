#Largest Element In an Array.
#input:nums=[1,2,3,1,6,2]
#output:6
nums=[1,2,3,1,6,2]
n=len(nums)
largest = nums[0]
for i in range(1,n):
    if nums[i] > largest:
      largest=nums[i]
print(largest)
    
