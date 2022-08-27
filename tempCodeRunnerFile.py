
    ef = enemy_file_create(en,enemy_hp)
    enemy_hp, life_points, mana_points = battle(enemy_hp,en,ef,life_points, mana_points)
    while int(enemy_hp) > 0: