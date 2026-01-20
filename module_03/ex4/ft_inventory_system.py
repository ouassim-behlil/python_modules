
def count_specific(data: dict, player: str, type: str, rarity: str) -> int:
    for item, count in data['players'][player]['items'].items():
        catalog_item = data['catalog'].get(item)
        if catalog_item.get('type') == type \
            and catalog_item.get('rarity') == rarity:
            return count
    return 0

def get_value(data: dict, type: str, rarity:str):
    for item in data['catalog'].values():
        if item['type'] == type and item['rarity'] == rarity:
            return item.get('value')

def get_total_inventory(data: dict, player: str):
    total = 0
    for item, count in data['players'].get(player)['items'].items():
        total += count * data['catalog'].get(item)['value']
    return total

def items_count(data: dict, player: str):
    count = 0
    for  n_items in data['players'].get(player)['items'].values():
        count += n_items
    return count

def count_category(data: str, player: str) -> dict[str, int]:
    count_per_category = {
        'weapon' : 0,
        'consumable' : 0,
        'armor': 0
    }
    for item, count in data['players'].get(player)['items'].items():
        if data['catalog'].get(item)['type'] == 'weapon':
            count_per_category['weapon'] += count
        elif data['catalog'].get(item)['type'] == 'consumable':
            count_per_category['consumable'] += count
        else:
            count_per_category['armor'] += count

    return count_per_category

def player_inventory(data: dict, player: str):
    print("=== Player Inventory System ===")

    print(f"\n=== {player}'s Inventory ===")
    count = count_specific(data, 'alice', 'weapon', 'rare')
    value = get_value(data, 'weapon', 'rare')

    print(f"sword (weapon, rare): {count}x @ {value} gold each = {count * value} gold")
    count =  count_specific(data, 'alice', 'consumable', 'common')
    value = get_value(data, 'consumable', 'common')

    print(f"potion (consumable, common): {count}x @ {value} gold each = {count * value} gold")

    count =  count_specific(data, 'alice', 'accessory', 'rare')
    value = get_value(data, 'accessory', 'rare')
    print(f"shield (accessory, rare): {count}x @ {value} gold each = {count * value} gold")
    
    total = get_total_inventory(data, 'alice')
    print(f"\nInventory value: {total} gold")

    count = items_count(data, 'alice')
    print(f"Item count: {count} items")

    count_by_type = count_category(data, 'alice')
    # print(count_by_type)   
    print(f"Categories: weapon({count_by_type['weapon']}), consumable({count_by_type['consumable']}), armor({count_by_type['armor']})")

if __name__ =="__main__":
    data = {
        'players': 
        {
            'alice': 
            {
                'items': 
                {
                    'pixel_sword': 1,
                    'code_bow': 1,
                    'health_byte': 5,
                    'quantum_ring': 3
                },
                'total_value': 1875,
                'item_count': 10
            },
            'bob':
            {
                'items':
                {
                    'code_bow': 3,
                    'pixel_sword': 2
                },
                'total_value': 900, 
                'item_count': 5
                },
                'charlie':
                {
                    'items':
                    {
                        'pixel_sword': 1,
                        'code_bow': 1
                    },
                    'total_value': 350,
                    'item_count': 2
                }, 'diana':
                {
                    'items':
                    {
                        'code_bow': 3,
                        'pixel_sword': 3,
                        'health_byte': 3,
                        'data_crystal': 3
                    },
                    'total_value': 4125,
                    'item_count': 12
                }
            },
            'catalog': 
            {
                'pixel_sword': 
                {
                    'type': 'weapon',
                    'value': 150,
                    'rarity': 'rare'
                },
                'quantum_ring':
                {
                    'type': 'accessory',
                    'value': 500,
                    'rarity': 'rare'
                },
                'health_byte':
                {
                    'type': 'consumable',
                    'value': 25,
                    'rarity': 'common'
                },
                'data_crystal':
                {
                    'type': 'material',
                    'value': 1000,
                    'rarity': 'legendary'
                },
                'code_bow':
                {
                    'type': 'weapon',
                    'value': 200,
                    'rarity': 'uncommon'
                }
            }
        }
    player_inventory(data, 'alice')