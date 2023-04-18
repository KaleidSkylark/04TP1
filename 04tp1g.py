while True:
    try:
        base_speed = float(input("Enter base attack speed of the character: "))
        if base_speed <= 0:
            raise ValueError("Base speed must be positive.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        bonus_speed_percent = float(input("Enter bonus speed percentage of the character: ")) / 100
        if bonus_speed_percent < 0:
            raise ValueError("Bonus speed percentage cannot be negative.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        character_level = int(input("Enter the level of the character: "))
        if character_level <= 0:
            raise ValueError("Character level must be positive.")
        break
    except ValueError as e:
        print(e)

current_speed = base_speed * (1 + (bonus_speed_percent * (character_level - 1)))
current_speed = round(current_speed, 3)

print(f"At level {character_level}, the character's speed is {current_speed}.")
