
def leftRotate(arr):
  n=len(arr)
  if n == 0:
    return arr
  
  temp = arr[0]
  for i in range(1,n):
    arr[i-1] = arr[i]
  arr[-1] = temp
  return arr
arr=[1,2,3,4,5]
ans = leftRotate(arr)
print("Left rotated by one place is:" ,ans)