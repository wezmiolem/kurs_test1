inventory = {'laptop': 'elektronika',
'klawiatura': 'elektronika', 'krzesło': 'meble', 'biurko': 'meble'}

updated_inventory = {}

for key, value in inventory.items():
    if value in updated_inventory.keys():
        updated_inventory[value].append(key)
    else:
        updated_inventory[value] = [key]

print(updated_inventory)