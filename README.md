# International University of Business Agriculture and Technology

**Assignment Title:** Adventure Guild Management System  
**Course Name:** Object Oriented Programming Lab  
**Course Code:** CSE-2384  

### Submitted To:
* **Name:** Dr. Md. Shafenoor Amin  
* **Designation:** Assistant Professor  
* **Department:** Department of CSE (IUBAT)  

### Submitted By:
| Name | Id |
| :--- | :--- |
| Robiul Islam | 25303039 |
| Md. Irfan Khan | 25303040 |
| Masuma Akter | 25303047 |

**Department of Computer Science and Engineering**

---

## Table of Contents

| Topic Name | Link |
| :--- | :--- |
| Implemented Class | [Go](#implemented-class)|
| OOP Features Used | [Go](#oop-features-used) |
| Program Output | [Go](#program-output) |
| Reflection | [Go](#reflection) |

---

## Implemented Class

| Class Name | Key Attributes | Key Methods | Purpose |
| :--- | :--- | :--- | :--- |
| **Inventory** | `owner_name`, `capacity`, `inventory_type`, `items` | `add_item()`, `remove_item()`, `list_items()` | Manages equipment and items owned by an adventurer. |
| **Item** | `name`, `item_type`, `value`, `durability` | `get_details()`, `use_item()`, `repair()` | Represents equipment, consumables, or loot rewards. |
| **Reward** | `gold`, `experience`, `bonus_item` | `add_bonus_gold()`, `get_total()`, `display_reward()` | Represents rewards granted upon quest completion. |
| **Rank** | `rank_name`, `min_exp`, `tier` | `get_rank_info()`, `promote_tier()`, `update_min_exp()` | Tracks adventurer tier status and promotion progress. |
| **Monster** | `name`, `monster_type`, `health_point`, `attack_power` | `take_damage()`, `attack()`, `get_status()` | Encapsulates combat entities encountered on quests. |
| **Quest** | `title`, `difficulty`, `reward`, `is_active`, `assigned_adventurers`, `completed_by` | `assign_to()`, `complete_by()`, `get_status()` | Defines objectives, reward allocations, and adventurer assignments. |
| **Adventurer** | `name`, `level`, `health_point`, `exp`, `gold`, `guild`, `rank`, `inventory` | `take_damage()`, `join_guild()`, `add_gold()`, `assign_rank()`, `perform_action()` | Parent class representing generic guild members. |
| **Warrior** | `stamina` *(inherits from Adventurer)* | `shield_block()`, `attack()`, `rest()`, `perform_action()` | Melee specialist child class utilizing stamina. |
| **Mage** | `mana` *(inherits from Adventurer)* | `cast_spell()`, `meditate()`, `perform_action()` | Spellcaster child class utilizing mana resources. |
| **Archer** | `agility` *(inherits from Adventurer)* | `shoot_arrow()`, `dodge()`, `perform_action()` | Ranged physical specialist child class using agility. |
| **Guild** | `name`, `location`, `total_funds`, `members`, `quests` | `add_member()`, `remove_member()`, `add_quest()`, `get_guild_summary()` | Central organizational unit managing members and quests. |

---

## OOP Features Used

* **Inheritance:** Implemented via the base parent class `Adventurer` and three specialized child classes: `Warrior`, `Mage`, and `Archer`. Each child inherits core functionality while introducing distinct attributes (`stamina`, `mana`, `agility`).
* **Composition:** Demonstrated by `Adventurer`, which directly instantiates and owns unique `Inventory` and `Rank` objects. The lifecycle of these components is directly tied to the lifetime of the `Adventurer`.
* **Association:**
  * `Guild` maintains lists referencing `Adventurer` and `Quest` instances.
  * `Quest` references assigned `Adventurer` objects and contains a `Reward` object.
  * `Adventurer` keeps a reference to their joined `Guild`.
* **Polymorphism:** Demonstrated through method overriding of `perform_action()` across `Warrior`, `Mage`, and `Archer`. When executing `perform_action()` across a collection of base `Adventurer` references, each subclass executes its own unique action.

---

## Program Output

<img src="Screenshot 2026-09-02 120611.png">
---

## Reflection

### What was the most difficult class to implement?
**Answer:** The `Quest` class was the most complex and difficult to implement because it serves as the central orchestration point between dynamic entities. Managing state transitions (such as transitioning a quest from active to completed) required handling multiple edge cases: ensuring an adventurer could not be assigned the same quest twice, handling multi-adventurer dynamic assignments via lists, and properly triggering reward distribution upon completion. Additionally, integrating the `Reward` object with the `Quest` class demanded careful memory and variable management to update individual `Adventurer` inventory and gold balances accurately without duplicating rewards or leaving unhandled null attributes.

### Which object-oriented concept was most useful?
**Answer:** Inheritance combined with Polymorphism was by far the most valuable concept in this system. Creating an abstract-style parent class `Adventurer` with child classes (`Warrior`, `Mage`, `Archer`) allowed the implementation of base attributes (`name`, `hp`, `gold`) once, eliminating redundant code. Polymorphism specifically excelled through the `perform_action()` method override. This enabled the main `Guild` class and execution loops to process a collection of diverse generic `Adventurer` objects seamlessly without needing conditional `if/else` logic to check specific member types at runtime.

### What would you improve if additional time were available?
**Answer:** Given additional time, the following enhancements would be prioritized:
1. **Data Persistence:** Implement database integration (SQLite) or file standard persistence (JSON) to save and load guild progress, adventurer states, and inventory data across multiple system runs.
2. **Advanced Combat Engine:** Expand the `Monster` interaction into a fully automated round-based combat loop utilizing precise calculations for physical defense, critical hits, evasion stats, and dynamic skill cooldowns.
3. **User Interface & Validation:** Build a robust Command-Line Interface (CLI) or graphical interface (GUI) with comprehensive input validation and `try-except` exception handling to gracefully recover from invalid operations (e.g., assigning dead adventurers to quests or overfilling inventory limits).
