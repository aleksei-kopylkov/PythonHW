# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

things_for_camp = {"палатка": 10, "спальный мешок": 7, "веревка": 2, "нож": 0.3,
                   "спрей от насекомых": 0.5, "куртка": 4,
                   "гитара": 5}
bag_capacity = 20
load = 0
for item in things_for_camp:
    load = things_for_camp[item]
    print(item)
    for next_item in things_for_camp:
        if next_item != item:
            if load + things_for_camp[next_item] <= bag_capacity:
                print(next_item)
                load += things_for_camp[next_item]
    print()
