def sum_to(n):
  sum = 0
  for n in range(1, n + 1):
    sum+=n
  return sum

def largest(nums):
  largest_num = 0;
  for n in nums:
    if n > largest_num:
      largest_num = n
  return largest_num

print(largest([1, 2, 3, 4, 0]))