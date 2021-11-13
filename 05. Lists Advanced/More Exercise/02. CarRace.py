nums = [int(x) for x in input().split()]
left_sum = 0
right_sum = 0
for i in range(len(nums)//2):
   if nums[i] == 0:
       left_sum *= 0.80
   else:
        left_sum += nums[i]
   if nums[-(i+1)] == 0:
       right_sum *= 0.80
   else:
       right_sum += nums[-(i+1)]

if left_sum > right_sum:
    print(f'The winner is right with total time: {right_sum:.1f}')
else:
    print(f'The winner is left with total time: {left_sum:.1f}') 