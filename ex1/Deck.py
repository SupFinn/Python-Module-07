from ex0.CreatureCard import Card, CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import List, Dict, Type
import math
import random


class Deck:
    def __init__(self):
        self.cards: List[Card] = []
        self.creature_cards: List[CreatureCard] = []
        self.spell_cards: List[SpellCard] = []
        self.artifact_cards: List[ArtifactCard] = []

        self.card_types = {
            CreatureCard: self.creature_cards,
            SpellCard: self.spell_cards,
            ArtifactCard: self.artifact_cards
            }

    def add_card(self, card: Card) -> None:
        for card_type, card_list in self.card_types.items():
            if isinstance(card, card_type):
                card_list.append(card)
        self.cards.append(card)


    def remove_card(self, card_name: str) -> bool:
        if card_name is None:
            print("Give a name Buddy.")
            return False

        for card_to_remove in self.cards:
            if card_to_remove.name == card_name:
                self.cards.remove(card_to_remove)

        for card_type, card_list in self.card_types.items():
            if isinstance(card_to_remove, card_type):
                card_list.remove(card_to_remove)
                return True
        print("Card Not Found 😒.")
        return False


    def shuffle(self) -> None:
        random.shuffle(self.cards)


    def draw_card(self) -> Card:
            card: Card = self.cards.pop()

            for card_type, cards_list in self.card_types.items():
                if isinstance(card, card_type):
                    cards_list.remove(card)
            
            return card


    def get_deck_stats(self) -> dict:
        total_mana_cost = sum([card.cost for card in self.cards])

        avg_cost: float = 0.0
        try:
            avg_cost = total_mana_cost / len(self.cards)
        except ZeroDivisionError:
            print("Cost can't be 0!")

        return {
            'total_cards': len(self.cards),
            'creatures': len(self.creature_cards),
            'spells': len(self.spell_cards),
            'artifacts': len(self.artifact_cards),
            'avg_cost': float(f"{avg_cost:.1f}")
            }