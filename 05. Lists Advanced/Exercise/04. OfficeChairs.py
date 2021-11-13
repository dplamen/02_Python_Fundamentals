rooms = int(input())
free_chairs = 0
shortage_flag = False
for i in range(1, rooms + 1):
    total_chairs, chairs_taken = input().split()
    free = len(total_chairs) - int(chairs_taken)
    if free < 0:
        print(f"{-free} more chairs needed in room {i}")
        shortage_flag = True
    else:
        free_chairs += free
if not shortage_flag:
    print(f"Game On, {free_chairs} free chairs left")
