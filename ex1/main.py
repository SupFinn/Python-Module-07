from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard, Card
from ex1.Deck import Deck
from enum import Enum
from typing import List, Dict

class Rarity(Enum):

    level_1 = "Common"
    level_2 = "Rare"
    level_3 = "Legendary"

def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    
    print("Building deck with different card types...")

    lightning_bolt = SpellCard("Lightning Bolt", 3, Rarity.level_1.value, "Deal 3 damage to target")
    mana_crystal = ArtifactCard("Mana Crystal", 2, Rarity.level_2.value, 5, "Permanent: +1 mana per turn")
    fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.level_3.value, 7, 5)

    print("Deck stats: ", end='')
    deck = Deck()
    for card in [lightning_bolt, mana_crystal, fire_dragon]:
        deck.add_card(card)
    print(deck.get_deck_stats())


if __name__ == "__main__":
    main()