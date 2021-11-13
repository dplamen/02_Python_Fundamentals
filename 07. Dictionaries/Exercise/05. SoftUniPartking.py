n = int(input())
parking_lot = {}
for i in range(n):
    line = input()
    if line.startswith('register'):
        command, name, plate = line.split()
        if name not in parking_lot:
            parking_lot[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot[name]}")

    elif line.startswith('unregister'):
        command, name = line.split()
        if name not in parking_lot:
            print(f"ERROR: user {name} not found")
        else:
            del parking_lot[name]
            print(f"{name} unregistered successfully")

for k, v in parking_lot.items():
    print(f'{k} => {v}')
