from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex0.main import Rarity
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from typing import List, Dict


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    lightning_bolt = SpellCard(
        "Lightning Bolt", 3, Rarity.level_1.value, "Deal 3 damage to target"
        )
    mana_crystal = ArtifactCard(
        "Mana Crystal", 2, Rarity.level_2.value, 5,
        "Permanent: +1 mana per turn"
        )
    fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.level_3.value, 7, 5)

    deck = Deck()
    cards: List[Card] = [fire_dragon, mana_crystal, lightning_bolt]

    for card in cards:
        deck.add_card(card)
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    battlefield: List[Card] = []
    mana: int = 15
    i: int = 0
    while i < len(cards):
        card_drawed: Card = deck.draw_card()
        card_name: str = card_drawed.name
        card_type: str = card_drawed.__class__.__name__

        print(f"Drew: {card_name} ({card_type[:-4]})")
        is_playable: bool = card_drawed.is_playable(mana)
        game_state: Dict = {
            'is_playable': is_playable,
            'available_mana': mana,
            'battlefield': battlefield
        }
        print(f"Play result: {card_drawed.play(game_state)}\n")
        mana: int = game_state['available_mana']
        i += 1

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
