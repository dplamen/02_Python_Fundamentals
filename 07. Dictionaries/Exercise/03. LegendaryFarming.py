def output(dictionary):
    for k, v in dictionary.items():
        print(f"{k}: {v}")


mapping = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
collect_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
collected = False
while True:
    items = input().split()
    for i in range(0, len(items), 2):
        item = items[i + 1].lower()
        quantity = int(items[i])
        if item not in collect_dict:
            collect_dict[item] = 0
        collect_dict[item] += quantity
        if item in mapping and collect_dict[item] >= 250:
            print(f'{mapping[item]} obtained!')
            collect_dict[item] -= 250
            collected = True
            break
    if collected:
        break

key_materials = {k: v for (k, v) in collect_dict.items() if k in mapping}
junk_materials = {k: v for (k, v) in collect_dict.items() if k not in mapping}
key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk_materials = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
output(key_materials)
output(junk_materials)

