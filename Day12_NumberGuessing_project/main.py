############# Scope #############

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function {enemies}")
#
# increase_enemies()
# print(f"enemies outside function {enemies}")

#Local scope - exists within function
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

#Global scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 3:
#         new_enemy = enemies[0]
#     print(new_enemy)

enemies = 1

def increase_enemies():
    # global enemies
    # enemies += 1
    print(f"enemies inside function {enemies}")
    return enemies + 1

new_enemies = increase_enemies()
print(f"enemies outside function {new_enemies}")

#Constants
PI = 3.14159