from ex0.CreatureCard import CreatureCard
from typing import Dict, List
from enum import Enum


class Rarity(Enum):
    level_1 = "common"
    level_2 = "rare"
    level_3 = "legendary"


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    battlefield: List = []

    fire_dragon_card = CreatureCard(
        "Fire Dragon", 5, Rarity.level_3.value, 7, 5
        )

    print("CreatureCard Info:")
    print(fire_dragon_card.get_card_info())

    player_mana: int = 6
    print(f"\nPlaying Fire Dragon with {player_mana} mana available:")
    is_playable: bool = fire_dragon_card.is_playable(player_mana)
    print(f"Playable: {is_playable}")
    game_stats: Dict = {
        'is_playable': is_playable,
        'available_mana': player_mana,
        'battlefield': battlefield
    }
    print("Play result: ", end='')
    print(fire_dragon_card.play(game_stats))

    goblin_warrior = CreatureCard(
        "Goblin Warrior", 2, Rarity.level_2.value, 3, 2
        )
    player2_mana: int = 3

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result: ", end='')
    print(fire_dragon_card.attack_target(goblin_warrior.name))

    print(f"\nTesting insufficient mana ({player2_mana} available):")
    is_playable: bool = fire_dragon_card.is_playable(player2_mana)
    print(f"Playable: {is_playable}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
