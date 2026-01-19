if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice = {'first_blood', 'pixel_perfect', 'speed_runner'}
    bob = {'level_master', 'boss_hunter', 'treasure_seeker', 'speed_runner'}
    charlie = {
        'treasure_seeker', 'speed_runner', 'boss_hunter',
        'combo_king', 'first_blood'
    }

    print("Player Alice achievements:", alice)
    print("Player Bob achievements:", bob)
    print("Player Charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")

    unique_acheivements = alice.union(bob).union(charlie)
    print("All unique achievements:", unique_acheivements)
    print("Total unique achievements:", len(unique_acheivements))

    common_acheivements = alice.intersection(bob).intersection(charlie)
    print("\nCommon to all players:", common_acheivements)

    rare_acheivements = (alice - bob - charlie) \
        | (bob - alice - charlie) | (charlie - alice - bob)
    print("Rare achievements (1 player):", rare_acheivements)

    alice_bob_common = alice & bob
    bob_unique = bob - alice
    alice_unique = alice - bob
    print("\nAlice vs Bob common:", alice_bob_common)
    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)
