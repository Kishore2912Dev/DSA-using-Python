class Solution:
  def getSingleElement(self,arr):
    xor = 0
    for num in arr:
      xor ^= num
    return xor
arr = [4,2,1,2,1]
obj = Solution()
ans = obj.getSingleElement(arr)
print("The Single Element is:",ans)