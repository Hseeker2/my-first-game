###Imported Modules
import random
import copy
### Game Classes
# Player class
class player:
    def __init__(self, name, hp, maxhp, damage, armor, magic, maxmagic, magicdmg, gold):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.damage = damage
        self.armor = armor
        self.magic = magic
        self.maxmagic = maxmagic
        self.magicdmg = magicdmg
        self.gold = gold

# Enemy class
class enemy:
    def __init__(self, name, hp, damage, gold):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.gold = gold

# Item class
class item:
    def ___init___(self, name, heal, maxhp_add, dmg):
        self.name = name
        self.maxhp_add = maxhp_add
        self.heal = heal
        self.dmg = dmg

# Game enemies templates
thief = enemy("Thief", 20, [0, 5, 0, 0, 0, 5, 5, 5, 10], 5)
corrupted_guard = enemy("Corrupt guard", 40, [0, 0, 0, 0, 10, 10, 10, 20], 15)
corrupted_knight = enemy("Corrupt knight", 80, [0, 0, 0, 15, 15, 15, 25], 30)
fire_giant = enemy("Fire Giant", 200, [0, 0, 0, 20, 20, 20, 30], 50)
ice_giant = enemy("Ice Giant", 200, [0, 0, 0, 20, 20, 20, 30], 50)
dark_giant = enemy("Dark Giant", 300, [0, 30, 30, 30, 30, 30, 60], 100)
ancient_dragon = enemy("Ancient Dragon", 1000, [0, 50, 50, 50, 50, 50, 100], 250)

### Game Functions:
# Save function:
def save():
    n = "\n"
    save1 = open("save.txt", "w")
    save1.writelines(village_travel + n)
    save1.writelines(game_advance + n)
    save1.writelines(player.name + n)
    save1.writelines(str(player.hp) + n)
    save1.writelines(str(player.maxhp) + n)
    save1.writelines(str(player.damage) + n)
    save1.writelines(str(player.armor) + n)
    save1.writelines(str(player.magic) + n)
    save1.writelines(str(player.maxmagic) + n)
    save1.writelines(str(player.magicdmg) + n)
    save1.writelines(str(player.gold) + n)
    save1.close()

# Merchant function:
def merchant():
    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
    while merch not in ("1", "2", "3", "4", "5", "exit"):
        print("invalid input, please try again.\n")
        merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
    while merch in ("1", "2", "3", "4", "5", "exit"):
        if merch == "1":
            if player.gold >= 15:
                player.hp = player.hp + 15
                if player.hp > player.maxhp:
                    player.hp = player.maxhp
                else:
                    player.hp = player.hp
                player.gold = player.gold - 10
                print("health potion purchased, Player's HP: " + str(player.hp))
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
            else:
                print("you don't have enough gold, sorry!")
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
        elif merch == "2":
            if player.gold >= 10:
                player.magic = player.magic + 10
                player.gold = player.gold - 10
                print("Magic potion purchased, Player's Magic: " + str(player.magic))
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
            else:
                print("you don't have enough gold, sorry!")
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
        elif merch == "3":
            if player.gold >= 20:
                player_damage = []
                for x in player.damage:
                    if x != 0:
                        x = x + 5
                        player_damage.append(x)
                    else:
                        x = 0
                        player_damage.append(x)
                player.damage = player_damage
                player.gold = player.gold - 10
                print("Now you have a better sword! Player's damage: " + str(player.damage))
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
            else:
                print("you don't have enough gold, sorry!")
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
        elif merch == "4":
            if player.gold >= 20:
                player.maxhp = player.maxhp + 5
                player.gold = player.gold - 20
                print("health enhancer purchased, Player's Max HP: " + str(player.maxhp))
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
            else:
                print("you don't have enough gold, sorry!")
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
        elif merch == "5":
            if player.gold >= 20:
                player.maxmagic = player.maxmagic + 5
                player.gold = player.gold - 20
                print("magic enhancer purchased, Player's Max magic: " + str(player.maxmagic))
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
            else:
                print("you don't have enough gold, sorry!")
                merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
                while merch not in ("1", "2", "3", "4", "5", "exit"):
                    print("invalid input, please try again.\n")
                    merch = input("choose what to buy:\n1-Healing potion (+15 health) Cost: 15 gold.\n2-Magic potion (+10 Magic) Cost: 15 gold.\n3-A better sword. (+5 damage) Cost: 20 gold.\n4-health enhancer (increases max health by 5): 20 gold.\n5-Magic enhancer (increases max magic by 5): 20 gold\nexit-Exit the merchant store.\n")
        else:
            print("thank you, come again!")
            break

# Combat function, executed when encountering an enemy
def combat(x1):
    if x1 == "1":
        enemies = random.choice([thief, corrupted_guard, corrupted_guard, thief, thief, thief, thief, thief, thief, thief])
        current_enemy = copy.deepcopy(enemies)
    elif x1 == "2":
        enemies = random.choice([thief, thief, thief, corrupted_guard, thief, corrupted_knight, corrupted_guard, thief, thief,thief])
        current_enemy = copy.deepcopy(enemies)
    elif x1 == "3":
        enemies = random.choice([thief, thief, thief, corrupted_guard, thief, corrupted_knight, corrupted_guard, corrupted_guard, thief, thief])
        current_enemy = copy.deepcopy(enemies)
    elif x1 == "4":
        enemies = random.choice([thief, thief, corrupted_guard, corrupted_knight, corrupted_guard, corrupted_knight, thief, corrupted_knight, corrupted_guard, thief])
        current_enemy = copy.deepcopy(enemies)
    elif x1 == "5":
        enemies = random.choice([thief, thief, corrupted_guard, corrupted_knight, corrupted_knight, corrupted_knight, thief, corrupted_knight, corrupted_guard, thief])
        current_enemy = copy.deepcopy(enemies)
    elif x1 == "6":
        enemies = fire_giant
        current_enemy = copy.deepcopy(enemies)
    elif x1 == "7":
        enemies = ice_giant
        current_enemy = copy.copy(enemies)
    elif x1 == "8":
        enemies = dark_giant
        current_enemy = copy.copy(enemies)
    else:
        enemies = ancient_dragon
        current_enemy = copy.copy(enemies)
    status = input("you encountered a " + current_enemy.name + "!! enemy HP: " + str(current_enemy.hp) + ", what do you want to do?\n1-Fight\n2-Run\n")
    while status not in ("1", "2"):
        print("invalid input, please try again.")
        status = input("1-Fight\n2-Run\n")
    if status == "1":
        while player.hp > 0 and current_enemy.hp > 0:
            combat1 = input("choose your move:\n1-Attack\n2-Defense\n3-Use Magic\n")
            while combat1 not in ("1", "2", "3"):
                print("invalid input, please try again.\n")
                combat1 = input("choose your move:\n1-Attack\n2-Defense\n3-Use Magic\n")
            if combat1 == "1":
                player_dmg = random.choice(player.damage)
                current_enemy.hp = current_enemy.hp - player_dmg
                if player_dmg == 0:
                    print("you swing your weapon at the " + current_enemy.name + ", but he dodged it!")
                elif player_dmg != 0 and player_dmg != max(player.damage):
                    print("you swing your sword at the " + current_enemy.name + "! direct hit... enemy HP left: " + str(current_enemy.hp))
                else:
                    print("you scored a critical hit at the " + current_enemy.name + "! enemy HP left: " + str(current_enemy.hp))
                if current_enemy.hp > 0:
                    damage = random.choice(current_enemy.damage)
                    player.hp = player.hp - damage
                    if player.hp > 0:
                        if damage == 0:
                            print("The " + current_enemy.name + " swings his weapon at you, but you dodged his attack!")
                        elif damage != 0 and damage != max(current_enemy.damage):
                            print("The " + current_enemy.name + " hits back! Player HP left: " + str(player.hp))
                        else:
                            print("you received a critical hit! that hurts... Player's HP left: " + str(player.hp))
                    else:
                        print("The " + current_enemy.name + " hits back! uh oh... looks like you're done for.")
                        print("You are dead... GAME OVER")
                        quit()
                        break
                else:
                    print("enemy down! Victory!")
                    player.gold = player.gold + current_enemy.gold
                    print("Reward: " + str(current_enemy.gold) + " Gold, you now have a total of: " + str(player.gold) + " gold.")
                    is_dead = 1
                    return is_dead
                    break
            elif combat1 == "2":
                damage = random.choice(current_enemy.damage)
                if player.armor >= damage:
                    print("you blocked the " + current_enemy.name + " attack.")
                else:
                    player.hp = player.hp - damage + player.armor
                    if player.hp > 0:
                        print("you took the hit... Player HP left: " + str(player.hp))
                    else:
                        print("you took the hit! uh oh... looks like you're done for.")
                        print("You are dead... GAME OVER")
                        quit()
                        break
            else:
                magic_move = input("choose your magic move:\n1-Wind blow. Cost: 15 magic\n2-Fire Storm. Cost: 20\n3-Ice Freeze. Cost: 25\n")
                while magic_move not in ("1", "2", "3"):
                    print("invalid input, please try again.")
                    magic_move = input("choose your magic move:\n1-Wind blow\n2-Fire Storm\n3-Shield\n")
                if magic_move == "1":
                    if player.magic >= 15:
                        current_enemy.hp = current_enemy.hp - (30 * player.magicdmg)
                        player.magic = player.magic - 15
                        if current_enemy.hp > 0:
                            print("you cast a spell that blows wind on the " + current_enemy.name + ", enemy HP left: " + str(current_enemy.hp))
                            damage = random.choice(current_enemy.damage)
                            player.hp = player.hp - damage
                            if player.hp > 0:
                                if damage == 0:
                                    print("The " + current_enemy.name + " swings his weapon at you, but you dodged his attack!")
                                elif damage != 0 and damage != max(current_enemy.damage):
                                    print("The " + current_enemy.name + " hits back! Player HP left: " + str(player.hp))
                                else:
                                    print("you received a critical hit! that hurts... Player's HP left: " + str(player.hp))
                            else:
                                print("The " + current_enemy.name + " hits back! uh oh... looks like you're done for.")
                                print("You are dead... GAME OVER")
                                quit()
                                break
                        else:
                            print("you cast a spell that blows wind on the " + current_enemy.name + ", enemy HP left: " + str(current_enemy.hp))
                            print("enemy down! Victory!")
                            is_dead = 1
                            player.gold = player.gold + current_enemy.gold
                            print("Reward: " + str(current_enemy.gold) + " Gold, you now have a total of: " + str(player.gold) + " gold.")
                            return is_dead
                    else:
                        print("you don't have enough magic to perform this attack!")
                elif magic_move == "2":
                    if player.magic >= 20:
                        current_enemy.hp = current_enemy.hp - (40 * player.magicdmg)
                        player.magic = player.magic - 20
                        if current_enemy.hp > 0:
                            print("you cast a spell that burns the " + current_enemy.name + " alive! enemy HP left: " + str(current_enemy.hp))
                            damage = random.choice(current_enemy.damage)
                            player.hp = player.hp - damage
                            if player.hp > 0:
                                if damage == 0:
                                    print("The " + current_enemy.name + " swings his weapon at you, but you dodged his attack!")
                                elif damage != 0 and damage != max(current_enemy.damage):
                                    print("The " + current_enemy.name + " hits back! Player HP left: " + str(player.hp))
                                else:
                                    print("you received a critical hit! that hurts... Player's HP left: " + str(player.hp))
                            else:
                                print("The " + current_enemy.name + " hits back! uh oh... looks like you're done for.")
                                print("You are dead... GAME OVER")
                                quit()
                                break
                        else:
                            print("you cast a spell that burns the " + current_enemy.name + " alive! enemy HP left: " + str(current_enemy.hp))
                            print("enemy down! Victory!")
                            is_dead = 1
                            player.gold = player.gold + current_enemy.gold
                            print("Reward: " + str(current_enemy.gold) + " Gold, you now have a total of: " + str(player.gold) + " gold.")
                            return is_dead
                    else:
                        print("you don't have enough magic to perform this attack!")
                else:
                    if player.magic >= 25:
                        current_enemy.hp = current_enemy.hp - (50 * player.magicdmg)
                        player.magic = player.magic - 25
                        if current_enemy.hp > 0:
                            print("you cast a spell that freezes the " + current_enemy.name + " stone cold! enemy HP left: " + str(current_enemy.hp))
                            damage = random.choice(current_enemy.damage)
                            player.hp = player.hp - damage
                            if player.hp > 0:
                                if damage == 0:
                                    print("The " + current_enemy.name + " swings his weapon at you, but you dodged his attack!")
                                elif damage != 0 and damage != max(current_enemy.damage):
                                    print("The " + current_enemy.name + " hits back! Player HP left: " + str(player.hp))
                                else:
                                    print("you received a critical hit! that hurts... Player's HP left: " + str(player.hp))
                            else:
                                print("The " + current_enemy.name + " hits back! uh oh... looks like you're done for.")
                                print("You are dead... GAME OVER")
                                quit()
                                break
                        else:
                            print("you cast a spell that freezes the " + current_enemy.name + " stone cold! enemy HP left: " + str(current_enemy.hp))
                            print("enemy down! Victory!")
                            is_dead = 1
                            player.gold = player.gold + current_enemy.gold
                            print("Reward: " + str(current_enemy.gold) + " Gold, you now have a total of: " + str(player.gold) + " gold.")
                            return is_dead
                    else:
                        print("you don't have enough magic to perform this attack!")
    else:
        is_dead = 0
        player.hp = player.hp - random.choice(current_enemy.damage)
        if player.gold > 0:
            player.gold = player.gold - current_enemy.gold
        else:
            player.gold = 0
        print("you escaped, but the thief managed to hit you as you were running away, and took some of your gold...\nPlayer's HP left: " + str(player.hp) + ", Player's gold: " + str(player.gold) + ".")
        return is_dead

# Traveling Function
def travel(village_travel):
    if game_advance == "1":
        if village_travel == "1":
            village_travel = "1"
            save()
            print("you decide to leave and head to the next village, it's located in the desert and called the Desert island...")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-stay in the Old village.\n2-head to the next land.\n")
            while village_travel not in ("1", "2"):
                village_travel = "1"
                save()
                print("that place doesn't exist... yet.")
                village_travel = input("now that you're out of the village, what do you want to do?\n1-stay in the Old village.\n2-head to the next land.\n")
            return village_travel
        elif village_travel == "2":
            village_travel = "2"
            save()
            print("you decide to leave and head to the next village...")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-head to the Old village.\n2-stay in the Desert land.\n3-head to the next land.\n")
            while village_travel not in ("1", "2", "3"):
                village_travel = "2"
                save()
                print("invalid input, please try again.")
                village_travel = input("what do you want# to do?\n1-head to the Old village.\n2-stay in the Desert land.\n3-head to the next land.\n")
            return village_travel
        elif village_travel == "3":
            village_travel = "3"
            save()
            print("you decide to leave and head to the next village...")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-stay in the Fire land.\n4-head to the next village.\n")
            while village_travel not in ("1", "2", "3", "4"):
                village_travel = "3"
                save()
                print("invalid input, please try again.")
                village_travel = input("what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-stay in the Fire land.\n4-head to the next village.\n")
            return village_travel
        elif village_travel == "4":
            village_travel = "4"
            save()
            print("you decide to leave and head to the next village...")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-head to the Fire land.\n4-stay in the Ice land.\n5-head to the next land.\n")
            while village_travel not in ("1", "2", "3", "4", "5"):
                village_travel = "4"
                save()
                print("invalid input, please try again.")
                village_travel = input("what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-head to the Fire land.\n4-stay in the Ice land.\n5-head to the next land.\n")
            return village_travel
        else:
            village_travel = "5"
            save()
            print("you decide to leave and head to the next village...")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-head to the Old village\n2-head to the Desert land.\n3-head to the Fire land.\n4-head to the Ice land.\n5-stay in the Dark.\n")
            while village_travel not in ("1", "2", "3", "4", "5"):
                village_travel = "5"
                save()
                print("invalid input, please try again.")
                village_travel = input("what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-head to the Fire land.\n4-head to the Ice land.\n5-stay in the Dark.\n")
            return village_travel
    else:
        if village_travel == "1":
            village_travel = "1"
            save()
            print("you decide to leave and head to the next village...")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-stay in the Old village.\n2-head to the Desert land.\n3-head to the Fire land.\n4-head to the Ice land.\n5-head to the Dark land.\n")
            while village_travel not in ("1", "2", "3", "4", "5"):
                village_travel = "1"
                save()
                print("that place doesn't exist... yet.")
                village_travel = input("what do you want to do?\n1-stay in the Old village.\n2-head to the Desert land.\n3-head to the Fire land.\n4-head to the Ice land.\n5-head to the Dark land.\n")
            return village_travel
        elif village_travel == "2":
            village_travel = "2"
            save()
            print("you decide to leave and head to the next village.")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-head to the Old village.\n2-stay in the Desert land.\n3-head to the Fire land.\n4-head to the Ice land.\n5-head to the Dark land.\n")
            while village_travel not in ("1", "2", "3", "4", "5"):
                village_travel = "2"
                save()
                print("invalid input, please try again.")
                village_travel = input("what do you want to do?\n1-head to the Old village.\n2-stay in the Desert land.\n3-head to the Fire land.\n4-head to the Ice land.\n5-head to the Dark land.\n")
            return village_travel
        elif village_travel == "3":
            village_travel = "3"
            save()
            print("you decide to leave and head to the next village.")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-stay in the Fire land.\n4-head to the Ice land.\n5-head to the Dark land.\n")
            while village_travel not in ("1", "2", "3", "4", "5"):
                village_travel = "3"
                save()
                print("invalid input, please try again.")
                village_travel = input("what do you want to do?\n1-head to the Old village\n2-head to the Desert land.\n3-stay in the Fire land.\n4-head to the Ice land.\n5-head to the Dark land.\n")
            return village_travel
        elif village_travel == "4":
            village_travel = "4"
            save()
            print("you decide to leave and head to the next village.")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-head to the Fire land.\n4-stay in the Ice land.\n5-head to the Dark land.\n")
            while village_travel not in ("1", "2", "3", "4", "5"):
                village_travel = "4"
                save()
                print("invalid input, please try again.")
                village_travel = input("what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-head to the Fire land.\n4-stay in the Ice land.\n5-head to the Dark land.\n")
            return village_travel
        else:
            village_travel = "5"
            save()
            print("you decide to leave and head to the next village...")
            village_travel = input("now that you're out of the village, what do you want to do?\n1-head to the Old village\n2-head to the Desert land.\n3-head to the Fire land.\n4-head to the Ice land.\n5-stay in the Dark land.\n")
            while village_travel not in ("1", "2", "3", "4", "5"):
                village_travel = "5"
                save()
                print("invalid input, please try again.")
                village_travel = input("what do you want to do?\n1-head to the Old village.\n2-head to the Desert land.\n3-head to the Fire land.\n4-head to the Ice land.\n5-stay in the Dark land.\n")
            return village_travel

### Lands and villages the player visits
# The Old Village
def old_village(x2):
    print("our story continues... you head towards your next destination until...")
    combat("1")
    village = input("you get to the Old village and ask around.\nwhat do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n")
    while village not in ("1", "2", "3"):
        print("invalid input, please try again.")
        village = input("you get to the village nearby and ask around.\nwhat do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n")
    while village in ("1", "2", "3"):
        if village == "1":
            print("you ask around and the villagers and they show you de way to the mountain of the ancient dragon.")
            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n")
            while village not in ("1", "2", "3"):
                print("invalid input, please try again.")
                village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n")
        elif village == "2":
            merchant()
            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n")
            while village not in ("1", "2", "3"):
                print("invalid input, please try again.")
                village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n")
        else:
            break

# The Desert Land
def desert_land(x2):
    print("our story continues... you head towards your next destination until...")
    combat("2")
    village = input("you get to the Desert land and ask around.\nwhat do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
    while village not in ("1", "2", "3", "4"):
        print("invalid input, please try again.")
        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
    while village in ("1", "2", "3", "4"):
        if village == "1":
            print("you ask around and the villagers and they tell you a story...(still need a story lol)")
            # needs a story
            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            while village not in ("1", "2", "3", "4"):
                print("invalid input, please try again.")
                village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
        elif village == "2":
            merchant()
            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            while village not in ("1", "2", "3", "4"):
                print("invalid input, please try again.")
                village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
        elif village == "3":
            break
        else:
            sub_mission = input("Choose one of the missions available in this town:\n1-Rescue a lost girl.\n2-Challenge the land's wisest man.\n3-Retrieve something stolen from a woman by the thieves.\n")
            while sub_mission not in ("1", "2", "3"):
                print("invalid input, please try again.")
                sub_mission = input("Choose one of the missions available in this town:\n1-Rescue a lost girl.\n2-Challenge the land's wisest man.\n3-Retrieve something stolen from a woman by the thieves.\n")
            if sub_mission == "1":
                challenge = input("you agreed to rescue a lost girl, you start looking around for her, her parent said she's somewhere in the desert out of the village. wanna go for it?\n1-yes\n2-no\n")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("wanna go for it?\n1-yes\n2-no")
                if challenge == "1":
                    print("you keep looking for the girl out in the desert until...")
                    combat("2")
                    print("you kept looking and found a thieves hideout! 3 enemies approach you: \"hey! what are you doing here!\"")
                    combat("2")
                    combat("2")
                    combat("2")
                    print("after killing all of them, you found the girl hidden inside their hideout! you returned the girl to her parent and they thanked you from the bottom of their heart.")
                    player.gold = player.gold + 30
                    print("here's your reward: 30 gold. Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                else:
                    print("the parent thanks you for stopping by, then go back to their endless sadness.")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            elif sub_mission == "2":
                print("you chose to challenge the land's wisest man! he will ask you questions, and you will get rewarded with 10 gold for every question answered correctly, but if you answer a question wrong, you will lose 5 gold!")
                challenge = input("do you accept?\n1-yes\n2-no\n")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no\n")
                if challenge == "1":
                    ques1 = input("first question, which is bigger?\n1-half of a quarter.\n2-quarter of a half.\n3-they're the same.\n")
                    if ques1 == "3":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    ques2 = input("second question, what's 9 times 8? don't use a calculator... i'm watching you!\n")
                    if ques2 == "72":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    ques3 = input("third question, what is 9 + 10 * 2 - 3?\n")
                    if ques3 == "26":
                        player.gold = player.gold + 10
                        print("great job! looks like someone was good at math in school! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! did you forget your math classes already? -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! did you forget your math classes already? -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    print("thanks for stopping by, see you later! Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                else:
                    print("oh well, suit yourself fella.")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            else:
                challenge = input("you have chosen to retrieve something stolen from an old lady by the thieves, it seems to be... a rubie? but she will reward you 30 gold if you get it back for her.\n1-yes\n2-no\n")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no")
                if challenge == "1":
                    print("the woman says her stolen thing is probably inside a locked cave, the cave won't open till you answer its riddle correctly.\nyou head to the cave and read the riddle:")
                    answer = input("I have cities but no houses, moutains but no trees, and water but no fish. What am I?\n")
                    while answer != "map" or answer != "exit":
                        print("that didn't seem to work... let's try again.")
                        answer = input("your answer: ")
                    if answer == "map":
                        player.gold = player.gold + 30
                        print("the door opens! you have successfully retrieved the old lady's... music box? oh well, she gives you 30 gold as a thanks.")
                        print("Player's total gold: " + str(player.gold) + ".")
                        village = int(input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n"))
                        while village not in ("1", "2", "3", "4"):
                            print("invalid input, please try again.")
                            village = int(input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n"))
                    else:
                        print("you decided it wasn't worth the time and left... but anyways, back to business.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                        while village not in ("1", "2", "3", "4"):
                            print("invalid input, please try again.")
                            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                else:
                    print("the old lady thanks you for stopping by and talking to her, even if it was for a short while.")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")

# The Fire Land
def fire_land(x2):
    print("our story continues... you head towards your next destination until...")
    combat("3")
    village = input("you get to the Fire land and ask around.\nwhat do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
    while village not in ("1", "2", "3", "4"):
        print("invalid input, please try again.")
        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
    while village in ("1", "2", "3", "4"):
        if village == "1":
            print("you ask around and the villagers and they tell you a story...")
            # needs a story
            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            while village not in ("1", "2", "3", "4"):
                print("invalid input, please try again.")
                village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
        elif village == "2":
            merchant()
            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            while village not in ("1", "2", "3", "4"):
                print("invalid input, please try again.")
                village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
        elif village == "3":
            break
        else:
            sub_mission = input("Choose one of the missions available in this town:\n1-Kill the Fire giant that's been scaring villagers.\n2-Challenge the land's wisest man.\n3-Retrieve something stolen from a villager.\n")
            while sub_mission not in ("1", "2", "3"):
                print("invalid input, please try again.")
                sub_mission = input("Choose one of the missions available in this town:\n1-Kill the Fire giant that's been scaring villagers.\n2-Challenge the land's wisest man.\n3-Retrieve something stolen from a villager.\n")
            if sub_mission == "1":
                print("you have chosen to kill the Fire giant, it's a tough foe, but the villagers will reward you generously, 50 gold and some goodies.")
                challenge = input("do you accept?\n1-yes\n2-no\n")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no\n")
                if challenge == "1":
                    print("you're on your way to fight the Fire giant...")
                    combat("6")
                    player.gold = player.gold + 50
                    print("after getting rid of the Fire Giant, the villagers rewarded you generously. Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                else:
                    print("on a second thought, you declined since it's seems to be a smart choice...")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            elif sub_mission == "2":
                print("you chose to challenge the land's wisest man! he will ask you questions, and you will get rewarded with 10 gold for every question answered correctly, but if you answer a question wrong, you will lose 5 gold!")
                challenge = input("do you accept?\n1-yes\n2-no\n")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no\n")
                if challenge == "1":
                    ques1 = input("first question, why can't you trust the law of gravity?\n1-because gravity is a hoax.\n2-because screw gravity.\n3-because it will always let you down.\n")
                    if ques1 == "3":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    ques2 = input("second question, What is lighter than a feather but the world’s strongest man can’t hold for Long?\n1-your breath.\2-the ozone layer.\3-ur teacher's mom, wise man my ass.\n")
                    if ques2 == "1":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    ques3 = input("third question, The more you take the more I leave behind. What am I?\n1-a hole\2-2-footsteps\n3-feces.\n")
                    if ques3 == "2":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    print("thanks for stopping by, see you later! Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                else:
                    print("oh well, suit yourself fella.")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            else:
                challenge = input("you have chosen to retrieve something stolen from an old lady by the thieves, it seems to be... an old staff? but she will reward you 50 gold if you get it back for her.\n1-yes\n2-no\n")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no")
                if challenge == "1":
                    print("you keep looking for the stolen thing around the land until...")
                    combat("3")
                    print("you kept looking and found a thieves hideout! 3 enemies approach you: \"hey! what are you doing here!\"")
                    combat("3")
                    print("after killing all of them, you found the stolen thing inside their hideout! you returned the stolen thing to its owner and they thanked you from the bottom of their heart.")
                    player.gold = player.gold + 50
                    print("here's your reward: 50 gold. Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                else:
                    print("the old lady thanks you for stopping by and talking to her, even if it was for a short while.")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")

# The Ice Land
def ice_land(x2):
    print("our story continues... you head towards your next destination until...")
    combat("4")
    village = input("you get to the Ice land and ask around.\nwhat do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
    while village not in ("1", "2", "3", "4"):
        print("invalid input, please try again.")
        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
    while village in ("1", "2", "3", "4"):
        if village == "1":
            print("you ask around and the villagers and they tell you a story... (still need a story lol)")
            # needs a story
            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            while village not in ("1", "2", "3", "4"):
                print("invalid input, please try again.")
                village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
        elif village == "2":
            merchant()
            village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            while village not in ("1", "2", "3", "4"):
                print("invalid input, please try again.")
                village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
        elif village == "3":
            break
        else:
            sub_mission = input("Choose one of the missions available in this town:\n1-Kill the Ice giant that's been scaring villagers.\n2-Challenge the land's wisest man.\n3-Retrieve something stolen from a villager.\n")
            while sub_mission not in ("1", "2", "3"):
                print("invalid input, please try again.")
                sub_mission = input("Choose one of the missions available in this town:\n1-Kill the Ice giant that's been scaring villagers.\n2-Challenge the land's wisest man.\n3-Retrieve something stolen from a villager.\n")
            if sub_mission == "1":
                print("you have chosen to kill the Ice giant, it's a tough foe, but the villagers will reward you generously, 70 gold and some goodies.")
                challenge = input("do you accept?\n1-yes\n2-no\n")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no\n")
                if challenge == "1":
                    print("you're on your way to fight the Ice giant...")
                    combat("7")
                    player.gold = player.gold + 70
                    print("after getting rid of the Ice Giant, the villagers rewarded you generously. Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                else:
                    print("on a second thought, you declined since it's seems to be a smart choice...")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
            elif sub_mission == "2":
                print("you chose to challenge the land's wisest man! he will ask you questions, and you will get rewarded with 10 gold for every question answered correctly, but if you answer a question wrong, you will lose 5 gold!")
                challenge = input("do you accept?\n1-yes\n2-no\n")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no\n")
                if challenge == "1":
                    ques1 = input("first question, what is 7+6/2+8? don't use a calculator... i'm watching you!\n")
                    if ques1 == "18":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! someone forgot their math classes... -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    ques2 = input("second question, Mr. and Mrs. Mustard have six daughters and each daughter has one brother. How many people are in the Mustard family?\n")
                    if ques2 == "9":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! think harder. -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    ques3 = input("third question, what's 7*6? again... no calculators.\n")
                    if ques3 == "42":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! practise more math... -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! practise more math... -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    print("thanks for stopping by, see you later! Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n")
                else:
                    print("oh well, suit yourself fella.")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.")
            else:
                challenge = input("you have chosen to retrieve something stolen from an old lady by the thieves, it seems to be... a golden ring? but she will reward you 70 gold if you get it back for her.\n1-yes\n2-no")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no")
                if challenge == "1":
                    print("you keep looking for the stolen thing around the land until...")
                    combat("4")
                    print("you kept looking and found a thieves hideout! 3 enemies approach you: \"hey! what are you doing here!\"")
                    combat("4")
                    print("after killing all of them, you found the stolen thing inside their hideout! you returned the stolen thing to its owner and they thanked you from the bottom of their heart.")
                    player.gold = player.gold + 70
                    print("here's your reward: 70 gold. Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.")
                else:
                    print("the old lady thanks you for stopping by and talking to her, even if it was for a short while.")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.")
                    while village not in ("1", "2", "3", "4"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.")

# The Dark Land
def dark_land(x2):
    print("our story continues... your search and all of your adventure has lead to this land, the dark land... the land where the dragon's mountain is.\nyou head towards your next destination until...")
    combat("5")
    village = input("you get to the Dark land and ask around.\nwhat do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
    while village not in ("1", "2", "3", "4", "5"):
        print("invalid input, please try again.")
        village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
    while village in ("1", "2", "3", "4", "5"):
        if village == "1":
            print("you ask around and the villagers and they told you a story...")
            # needs a story
            village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
            while village not in ("1", "2", "3", "4", "5"):
                print("invalid input, please try again.")
                village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
        elif village == "2":
            merchant()
            village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
            while village not in ("1", "2", "3", "4", "5"):
                print("invalid input, please try again.")
                village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
        elif village == "3":
            break
        elif village == "4":
            sub_mission = input("Choose one of the missions available in this town:\n1-Kill the Dark Giant that's been scaring villagers.\n2-Challenge the land's wisest man.\n3-Retrieve something stolen from a villager.\n")
            while sub_mission not in ("1", "2", "3"):
                print("invalid input, please try again.")
                sub_mission = input("Choose one of the missions available in this town:\n1-Kill the Dark giant that's been scaring villagers.\n2-Challenge the land's wisest man.\n3-Retrieve something stolen from a villager.\n")
            if sub_mission == "1":
                print("you have chosen to kill the Dark giant, it's a tough foe, but the villagers will reward you generously, 100 gold and some goodies.")
                challenge = input("do you accept?\n1-yes\n2-no")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no")
                if challenge == "1":
                    print("you're on your way to fight the fire giant...")
                    combat("8")
                    player.gold = player.gold + 100
                    print("after getting rid of the Dark Giant, the villagers rewarded you generously. Player's total gold: " + str(
                            player.gold) + ".")
                    village = input("what do you want to do?:\n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                    while village not in ("1", "2", "3", "4", "5"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                else:
                    print("on a second thought, you declined since it's seems to be a smart choice...")
                    village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                    while village not in ("1", "2", "3", "4", "5"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
            elif sub_mission == "2":
                print("you chose to challenge the land's wisest man! he will ask you questions, and you will get rewarded with 10 gold for every question answered correctly, but if you answer a question wrong, you will lose 5 gold!")
                challenge = input("do you accept?\n1-yes\n2-no")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no")
                if challenge == "1":
                    ques1 = int(input("first question, what is France's capital? no cheating...\n1-Lyon.\n2-Paris.\n3-Belgium"))
                    if ques1 == "2":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! someone forgot their math classes... -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    ques2 = int(input("second question, where is Taj Mahel located? no cheating...\n1-Pakistan\n2-South Africa\n3-India"))
                    if ques2 == "3":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! think harder. -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    ques3 = int(input("third question, what's 12+2*4/2+5"))
                    if ques3 == "19":
                        player.gold = player.gold + 10
                        print("you got this one correct! +10 gold.")
                    else:
                        if player.gold >= 5:
                            player.gold = player.gold - 5
                            print("nope, wrong answer! practise more math... -5 gold.")
                        else:
                            player.gold = 0
                            print("nope, wrong answer! practise more math... -5 gold.")
                            print("awwwe you're out of money! better luck next time!")
                    print("thanks for stopping by, see you later! Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                    while village not in ("1", "2", "3", "4", "5"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                else:
                    print("oh well, suit yourself fella.")
                    village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                    while village not in ("1", "2", "3", "4", "5"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
            else:
                challenge = input("you have chosen to retrieve something stolen from an old lady by the thieves, it seems to be... a necklace? but she will reward you 100 gold if you get it back for her.\n1-yes\n2-no")
                while challenge not in ("1", "2"):
                    print("invalid input, please try again.")
                    challenge = input("do you accept?\n1-yes\n2-no")
                if challenge == "1":
                    print("you keep looking for the stolen thing around the land until...")
                    combat("5")
                    print("you kept looking and found a thieves hideout! 3 enemies approach you: \"hey! what are you doing here!\"")
                    combat("5")
                    print("after killing all of them, you found the stolen thing inside their hideout! you returned the stolen thing to its owner and they thanked you from the bottom of their heart.")
                    player.gold = player.gold + 100
                    print("here's your reward: 100 gold. Player's total gold: " + str(player.gold) + ".")
                    village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                    while village not in ("1", "2", "3", "4", "5"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                else:
                    print("the parent thanks you for stopping by, then go back to their endless sadness.")
                    village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                    while village not in ("1", "2", "3", "4", "5"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
        else:
            print("you head on your way to face your final foe and rescue the princess, but on your way you find some company (of course lmao).")
            combat("5")
            combat("5")
            combat("5")
            combat("5")
            combat("5")
            print("well that was quite a lot... now you're heading to face the dragon... you still have a chance to go back and prepare yourself more.")
            challenge = input("do you accept to face the dragon?\n1-yes\n-no\n")
            if challenge == "1":
                is_dead = combat("9")
                if is_dead == 1:
                    print("you did it!! you killed the dragon and rescued the princess!! Congratulations, you have finished the game!")
                    print("there is a bit more to explore if you wish, you can redo this boss battle at anytime if you choose.")
                    end_game = input("do you want to go back to the village and build yourself to be the strongest warrior? or have you had enough for now:\nyes, return to the Dark land.\nno, I had enough with the game thank you.")
                    if end_game == "1":
                        village = input("you're now back to the village! what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                        while village not in ("1", "2", "3", "4", "5"):
                            print("invalid input, please try again.")
                            village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                    else:
                        print("ah i see, i hope you enjoyed the game! thank you for playing!!")
                        quit()
                        break
                else:
                    print("you escaped... you should be better prepared next time.")
                    village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                    while village not in ("1", "2", "3", "4", "5"):
                        print("invalid input, please try again.")
                        village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
            else:
                print("on a second thought, you decided not to do that since it seemed like a good idea...")
                village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")
                while village not in ("1", "2", "3", "4", "5"):
                    print("invalid input, please try again.")
                    village = input("what do you want to do?: \n1-Ask a villager about what happened.\n2-visit the merchant.\n3-continue your journey to the next village.\n4-Do a sub-mission.\n5-Face your fears (aka the dragon).\n")

### The beginning of the game
print("Welcome to my first game ever!")
print("1- New Game")
print("2- Load Game (still under work).")
print("3- Survival Mode(still under work).")
game_start = input("what do you want to do? type the number corresponding to the action: ")
while game_start not in ("1", "2", "3"):
    print("invalid input, please try again.")
    game_start = input("what do you want to do? type the number corresponding to the action: ")
if game_start == "1":
    class_select = input("select a class: \n1-Human (HP: 100, MaxHP: 100, Damage: 15, Armor: 20, Magic: 40)\n2-Vampire (HP: 120, MaxHP: 120, Damage: 20, Armor: 10, Magic: 20)\n3-Mage (HP: 80, MaxHP: 80, Damage: 10, Armor: 20, Magic: 100)\n4-Troll (HP: 120, MaxHP: 120, Damage: 25, Armor: 30, Magic: 10)\n")
    while class_select not in ("1", "2", "3", "4"):
        print("invalid input, please try again.")
        class_select = input("select a class: \n1-Human (HP: 100, MaxHP: 100, Damage: 15, Armor: 20, Magic: 60, Max Magic: 60)\n2-Vampire (HP: 120, MaxHP: 120, Damage: 20, Armor: 10, Magic: 40, Max Magic: 40)\n3-Mage (HP: 80, MaxHP: 80, Damage: 10, Armor: 20, Magic: 100, Max Magic: 100)\n4-Troll (HP: 120, MaxHP: 120, Damage: 25, Armor: 30, Magic: 40, Max Magic: 40)\n")
    if class_select == "1":
        print("you have chosen: Human")
        player = player(input("what would you like your character to be called?:\n"), 100, 100, [0, 15, 15, 15, 30], 20, 60, 60, 1, 10)
    elif class_select == "2":
        print("you have chosen: Vampire")
        player = player(input("what would you like your character to be called?:\n"), 120, 120, [0, 20, 20, 20, 40], 10, 40, 40, 1, 10)
    elif class_select == "3":
        print("you have chosen: Mage")
        player = player(input("what would you like your character to be called?:\n"), 80, 80, [0, 10, 10, 10, 20], 20, 100, 100, 2, 10)
    else:
        print("you have chosen: Troll")
        player = player(input("what would you like your character to be called?:\n"), 120, 120, [0, 25, 25, 25, 50], 30, 40, 40, 1, 10)
    print("so our adventure begins!")
    print("you wake up one day and receive a letter from the mail, it reads: \n" + player.name + ",\nyou've been chosen between thousands of warriors to be the one who rescues \nthe king's daughter from the ancient dragon, prepare yourself, your journey to save her begins today!")
    print("you carry your sword and shield and head on your way to save the king's daughter...")
    print("you head to the old village to ask around and know more about what happened to the king's daughter.")
    game_advance = "1"
    village_travel = "1"
    old_village("1")
    village_travel = travel(village_travel)
    while village_travel in ("1", "2", "3", "4", "5"):
        if village_travel == "1":
            old_village("1")
            village_travel = travel(village_travel)
        elif village_travel == "2":
            desert_land("2")
            village_travel = travel(village_travel)
        elif village_travel == "3":
            fire_land(village_travel)
            village_travel = travel(village_travel)
        elif village_travel == "4":
            ice_land("4")
            village_travel = travel(village_travel)
        else:
            game_advance = "2"
            dark_land("5")
            village_travel = travel(village_travel)

elif game_start == "2":
    print("coming soon!!")

    #try:
    #    load = open("save.txt", "r")
    #    village_travel = load.readlines()[0]
    #    game_advance = load.readlines()[1]
    #    player.name = str(load.readlines()[2])
    #    player.hp = int(load.readlines()[3])
    #    player.maxhp = int(load.readlines()[4])
    #    player.damage = load.readlines()[5]
    #    player.armor = int(load.readlines()[6])
    #    player.magic = int(load.readlines()[7])
    #    player.maxmagic = int(load.readlines()[8])
    #    player.magicdmg = int(load.readlines()[9])
    #    player.gold = int(load.readlines()[10])
    #    load.close()
    #    while village_travel in ("1", "2", "3", "4", "5"):
    #        if village_travel == "1":
    #            old_village("1")
    #            village_travel = travel(village_travel)
    #        elif village_travel == "2":
    #            desert_land("2")
    #            village_travel = travel(village_travel)
    #        elif village_travel == "3":
    #            fire_land(village_travel)
    #            village_travel = travel(village_travel)
    #        elif village_travel == "4":
    #            ice_land("4")
    #            village_travel = travel(village_travel)
    #        else:
    #            game_advance = "2"
    #            dark_land("5")
    #            village_travel = travel(village_travel)
    #except FileNotFoundError:
    #    print("you have no saved data! please play the game first.")
    #    quit()

else:
    print("coming soon!!")
