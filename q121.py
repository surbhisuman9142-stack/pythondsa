def binarysearch(target,num):
 left = 0
 right = len(num) - 1
 while left <= right:
  middle = (left + right ) // 2
  if num[middle] == target:
   return middle
  elif target < num[middle]:
   right = middle - 1
  else:
   left = middle + 1
 return -1
num = [1, 3, 5, 7, 9]
target = 7

print(binarysearch(target, num))