from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex1.main import Rarity
from typing import List, Dict
from ex0.CreatureCard import CreatureCard

def get_class_methods(cls) -> list:
    return [name for name in dir(cls)
               if not name.startswith('_') and callable(getattr(cls, name))]


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print(f"- Card: {get_class_methods(Card)}")
    print(f"- Combatable: {get_class_methods(Combatable)}")
    print(f"- Magical: {get_class_methods(Magical)}")

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    arcane_warrior = EliteCard("Arcane Warrior", 10, Rarity.level_3.value, 5,
                                5, 15)
    enemy: EliteCard = EliteCard("Enemy", 7,
                                 Rarity.level_2.value, 7, 0, 10)

    available_mana_1: int = 20
    battlefield: List[Card] = []
    game_state: dict = {
            'is_playable': arcane_warrior.is_playable(available_mana_1),
            'available_mana': available_mana_1,
            'battlefield': battlefield
            }
    arcane_warrior.play(game_state)

    available_mana_2: int = 15
    game_state: dict = {
            'is_playable': enemy.is_playable(available_mana_2),
            'available_mana': available_mana_2,
            'battlefield': battlefield
            }
    enemy.play(game_state)
  
    print(f"Attack result: {arcane_warrior.attack(enemy)}")
    print(f"Defense result: {arcane_warrior.defend(enemy.attack_power)}")

    enemy1: CreatureCard = CreatureCard("Enemy1", 4,
                                        Rarity.level_1.value, 2, 2)
    enemy2: CreatureCard = CreatureCard("Enemy2", 3,
                                        Rarity.level_2.value, 3, 3)


    print("\nMagic phase:")
    print(f"Spell cast: {arcane_warrior.cast_spell("Fireball", [enemy1.name, enemy2.name])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()