
# 1. INVENTORY CLASS

class Inventory:
    def __init__(self, owner_name, capacity=10, inventory_type="General"):
        self.owner_name = owner_name
        self.capacity = capacity
        self.inventory_type = inventory_type
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            return f"{item.name} added to {self.owner_name}'s inventory."
        return f"{self.owner_name}'s inventory is full."

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return f"{item_name} removed from {self.owner_name}'s inventory."
        return f"{item_name} not found in {self.owner_name}'s inventory."

    def list_items(self):
        if not self.items:
            return f"{self.owner_name}'s inventory is empty."
        item_list = ", ".join([item.name for item in self.items])
        return f"{self.owner_name}'s Inventory ({self.inventory_type}): {item_list}"



# 2. ITEM CLASS

class Item:
    def __init__(self, name, item_type, value, durability=100):
        self.name = name
        self.item_type = item_type
        self.value = value
        self.durability = durability

    def get_details(self):
        return f"Item: {self.name}, Type: {self.item_type}, Value: {self.value}"

    def use_item(self):
        if self.durability > 0:
            self.durability = max(0, self.durability - 10)
            return f"{self.name} used. Durability is now {self.durability}."
        return f"{self.name} is broken and cannot be used."

    def repair(self, amount=20):
        self.durability = min(100, self.durability + amount)
        return f"{self.name} repaired to {self.durability} durability."



# 3. REWARD CLASS

class Reward:      
    def __init__(self, gold, experience, bonus_item):
        self.gold = gold
        self.experience = experience
        self.bonus_item = bonus_item

    def add_bonus_gold(self, gold):
        self.gold += gold
        return f"Bonus gold added! Total Gold: {self.gold}"

    def get_total(self):
        return self.gold + self.experience

    def display_reward(self):
        return f"Gold: {self.gold}, EXP: {self.experience}, Bonus Item: {self.bonus_item.name}"



#4. RANK CLASS

class Rank:
    def __init__(self, rank_name, min_exp, tier):
        self.rank_name = rank_name
        self.min_exp = min_exp
        self.tier = tier

    def get_rank_info(self):
        return f"Rank: {self.rank_name} (Tier {self.tier}) - Req EXP: {self.min_exp}"

    def promote_tier(self):
        self.tier += 1
        return f"{self.rank_name} promoted to Tier {self.tier}."

    def update_min_exp(self, new_exp):
        self.min_exp = new_exp
        return f"{self.rank_name} now requires {self.min_exp} EXP for promotion."

# 5. MONSTER CLASS

class Monster:
    def __init__(self, name, monster_type, health_point, attack_power=15):
        self.name = name
        self.monster_type = monster_type
        self.health_point = health_point
        self.attack_power = attack_power

    def take_damage(self, amount):
        if amount > 0:
            self.health_point = max(0, self.health_point - amount)
        return f"{self.name} took {amount} damage. Health: {self.health_point}"

    def attack(self, target):
        target.take_damage(self.attack_power)
        return f"{self.name} attacks {target.name} for {self.attack_power} damage!"

    def get_status(self):
        return f"Monster: {self.name} ({self.monster_type}) | Health: {self.health_point}"

# 6. QUEST CLASS

class Quest:
    def __init__(self, title, difficulty, reward, is_active=True):
        self.title = title
        self.difficulty = difficulty
        self.reward = reward
        self.is_active = is_active
        self.assigned_adventurers = []
        self.completed_by = []

    def assign_to(self, adventurer):
        if adventurer in self.assigned_adventurers:
            return f"{adventurer.name} is already assigned to {self.title}."
        self.assigned_adventurers.append(adventurer)
        return f"{self.title} assigned to {adventurer.name}."

    def complete_by(self, adventurer):
        if adventurer not in self.assigned_adventurers:
            return False, f"{adventurer.name} is not assigned to {self.title}."
        if adventurer in self.completed_by:
            return False, f"{adventurer.name} already completed {self.title}."
        self.completed_by.append(adventurer)
        return True, f"{adventurer.name} completed {self.title}."

    def get_status(self):
        return (
            f"Quest {self.title} | Difficulty: {self.difficulty} | "
            f"Assigned: {len(self.assigned_adventurers)} | Completed: {len(self.completed_by)}"
        )


# 7. ADVENTURER PARENT CLASS

class Adventurer:
    def __init__(self, name, level, health_point, exp=0):
        self.name = name
        self.level = level
        self.health_point = health_point
        self.exp = exp
        self.gold = 0
        self.guild = None
        self.rank = Rank("Bronze Adventurer", 0, 1)  # Composition: Default Rank
        self.inventory = Inventory(name)              # Composition: Own Inventory

    def take_damage(self, amount):
        if amount > 0:
            self.health_point -= amount
        return f"{self.name} took {amount} damage. Current Health: {self.health_point}"

    def join_guild(self, guild):
        self.guild = guild
        return f"{self.name} joined {guild.name}."

    def add_gold(self, amount):
        self.gold += amount
        return f"{self.name} earned {amount} gold. Total Gold: {self.gold}"

    def assign_rank(self, new_rank):
        self.rank = new_rank
        return f"{self.name} has been assigned the rank: {self.rank.rank_name} (Tier {self.rank.tier})"

    def perform_action(self):
        return f"{self.name} prepares for action!"



# 8. WARRIOR CLASS (CHILD CLASS 1)

class Warrior(Adventurer):
    def __init__(self, name, level, health_point, stamina=30):
        super().__init__(name, level, health_point)
        self.stamina = stamina

    def shield_block(self):
        return f"{self.name} uses Shield Block to reduce incoming damage!"

    def attack(self, target):
        if self.stamina >= 10:
            self.stamina -= 10
            damage = 20 + (self.level * 2)
            target.take_damage(damage)
            return f"{self.name} attacks {target.name} for {damage} damage! Stamina left: {self.stamina}"
        return f"{self.name} is too tired to attack. Stamina left: {self.stamina}"

    def rest(self):
        self.stamina += 20
        return f"{self.name} rests and recovers stamina. Current Stamina: {self.stamina}"

    def perform_action(self):
        return f"{self.name} swings their heavy sword with great force!"


# 9. MAGE CLASS (CHILD CLASS 2)

class Mage(Adventurer):
    def __init__(self, name, level, health_point, mana=40):
        super().__init__(name, level, health_point)
        self.mana = mana

    def cast_spell(self, spell_name, target):
        if self.mana >= 15:
            self.mana -= 15
            damage = 25 + (self.level * 3)
            target.take_damage(damage)
            return f"{self.name} casts {spell_name} on {target.name} for {damage} damage! Mana left: {self.mana}"
        return f"{self.name} does not have enough mana to cast {spell_name}. Mana left: {self.mana}"

    def meditate(self):
        self.mana += 30
        return f"{self.name} meditates and recovers mana. Current Mana: {self.mana}"

    def perform_action(self):
        return f"{self.name} conjures a glowing mystic spell!"


# 10. ARCHER CLASS (CHILD CLASS 3)

class Archer(Adventurer):
    def __init__(self, name, level, health_point, agility=25):
        super().__init__(name, level, health_point)
        self.agility = agility

    def shoot_arrow(self, target):
        if self.agility >= 5:
            self.agility -= 5
            damage = 15 + (self.level * 2)
            target.take_damage(damage)
            return f"{self.name} shoots an arrow at {target.name} for {damage} damage! Agility left: {self.agility}"
        return f"{self.name} is too tired to shoot an arrow. Agility left: {self.agility}"

    def dodge(self):
        self.agility += 10
        return f"{self.name} dodges gracefully. Current Agility: {self.agility}"

    def perform_action(self):
        return f"{self.name} takes aim and releases a precise shot!"


# GUILD CLASS

class Guild:
    def __init__(self, name, location="Tamriel Hub", total_funds=1000):
        self.name = name
        self.location = location
        self.total_funds = total_funds
        self.members = []
        self.quests = []

    def add_member(self, adventurer):
        if adventurer not in self.members:
            self.members.append(adventurer)
            adventurer.join_guild(self)
            return f"{adventurer.name} added to {self.name}."
        return f"{adventurer.name} is already a member of {self.name}."

    def remove_member(self, adventurer):
        if adventurer in self.members:
            self.members.remove(adventurer)
            adventurer.guild = None
            return f"{adventurer.name} removed from {self.name}."
        return f"{adventurer.name} is not a member of {self.name}."

    def add_quest(self, quest):
        if quest not in self.quests:
            self.quests.append(quest)
            return f"Quest '{quest.title}' added to {self.name}."
        return f"Quest '{quest.title}' is already in {self.name}."

    def get_guild_summary(self):
        return f"Guild: {self.name} | Location: {self.location} | Members: {len(self.members)} | Quests: {len(self.quests)}"



# MAIN DEMONSTRATION FUNCTION

def main():
    print("1. CREATION OF GUILDS & ITEMS")
    guild = Guild("Phoenix Guild", location="Whiterun")
    dragon_scale = Item("Dragon Scale", "Material", 200)
    iron_sword = Item("Iron Sword", "Weapon", 50)
    elven_bow = Item("Elven Bow", "Weapon", 90)

    print("2. CREATION OF ADVENTURERS (INHERITANCE)")
    warrior = Warrior("Arthur", level=5, health_point=100, stamina=30)
    mage = Mage("Merlin", level=5, health_point=70, mana=40)
    archer = Archer("Robin", level=5, health_point=80, agility=25)

    print(guild.add_member(warrior))
    print(guild.add_member(mage))
    print(guild.add_member(archer))

    print("3. CREATION & ASSIGNMENT OF QUESTS")
    reward = Reward(gold=150, experience=300, bonus_item=dragon_scale)
    slay_dragon = Quest("Slay the Dragon", "Hard", reward)
    print(guild.add_quest(slay_dragon))
    print(slay_dragon.assign_to(archer))
    print(slay_dragon.get_status())

    print(" 4. INVENTORY MANAGEMENT & COMPOSITION")
    print(warrior.inventory.add_item(iron_sword))
    print(archer.inventory.add_item(elven_bow))
    print(archer.inventory.list_items())

    print("5. QUEST COMPLETION & REWARD DISTRIBUTION")
    success, msg = slay_dragon.complete_by(archer)
    print(msg)
    if success:
        print(archer.add_gold(reward.gold))
        print(archer.inventory.add_item(reward.bonus_item))

    print("6. COMBAT & MONSTER DEMO")
    goblin = Monster("Goblin Chief", "Beast", health_point=100, attack_power=15)
    print(goblin.get_status())
    print(warrior.attack(goblin))
    print(goblin.get_status())
    print(goblin.attack(warrior))

    print("7. MEMBER RANKINGS & ASSIGNMENT")
    gold_rank = Rank("Gold Adventurer", min_exp=1000, tier=1)
    print(gold_rank.get_rank_info())
    print(archer.assign_rank(gold_rank))
    print(archer.rank.get_rank_info())
    print(guild.get_guild_summary())

    print("8. POLYMORPHISM DEMONSTRATION ")
    party = [warrior, mage, archer]
    for adventurer in party:
        print(adventurer.perform_action())


if __name__ == "__main__":
    main()