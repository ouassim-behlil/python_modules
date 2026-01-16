if __name__ == "__main__":
    data = {
        'alice': [
            'first_blood', 'pixel_perfect', 'speed_runner',
            'first_blood', 'first_blood'
        ],
        'bob': [
            'level_master', 'boss_hunter', 'treasure_seeker',
            'level_master', 'level_master'
        ],
        'charlie': [
            'treasure_seeker', 'boss_hunter', 'combo_king', 'first_blood',
            'boss_hunter', 'first_blood', 'boss_hunter', 'first_blood'
        ],
        'diana': [
            'first_blood', 'combo_king', 'level_master', 'treasure_seeker',
            'speed_runner', 'combo_king', 'combo_king', 'level_master'
        ],
        'eve': [
            'level_master', 'treasure_seeker', 'first_blood',
            'treasure_seeker', 'first_blood', 'treasure_seeker'
        ],
        'frank': [
            'explorer', 'boss_hunter', 'first_blood',
            'explorer', 'first_blood', 'boss_hunter'
        ]
        }

    for key, value in data.items():
        print(f"Player {key} achievements:", set(value))

    print("\n=== Achievement Analytics ===")

    unique_acheivements = set()
    common_acheivements = set(data['alice'])
    for acheivement in data.values():
        unique_acheivements = unique_acheivements.union(set(acheivement))
        common_acheivements = common_acheivements.intersection(
            set(acheivement)
        )
    print("All unique achievements:", unique_acheivements)
    print("Total unique achievements:", len(unique_acheivements))

    print("\nCommon to all players:", common_acheivements)
    rare_acheivements = set()
    for player in data.keys():
        temp = set(data[player])
        for p, acheivement in data.items():
            if p != player:
                temp = temp - set(acheivement)
        rare_acheivements |= temp
    print("Rare achievements (1 player):", rare_acheivements)

    alice_bob_common = set(data['alice']) & set(data['bob'])
    bob_unique = set(data['bob']) - set(data['alice'])
    alice_unique = set(data['alice']) - set(data['bob'])
    print("\nAlice vs Bob common:", alice_bob_common)
    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)
