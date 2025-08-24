def flames_game():
    name1 = input("Enter first name: ").strip().lower()
    name2 = input("Enter second name: ").strip().lower()

    name2_list = list(name2)
    count = 0
    for ch in name1:
        if ch in name2_list:
            name2_list.remove(ch)
            count += 1

    v = len(name1) + len(name2) - 2 * count
    flames = list("FLAMES")
    index = 0

    while len(flames) > 1:
        index = (index + v - 1) % len(flames)
        print(f"Character {flames[index]} is deleted")
        flames.pop(index)

    result_map = {
        'F': "Friends",
        'L': "Lovers",
        'A': "Affection (Crush)",
        'M': "Marriage",
        'E': "Enemy",
        'S': "Siblings"
    }

    print(result_map[flames[0]])

flames_game()
