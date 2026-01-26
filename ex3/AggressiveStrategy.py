from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from typing import List

class AggressiveStrategy:
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played: List[Card]= []
        mana_used: int = 0
        damage_dealt: int = 0
        targets_attacked = []
        available_mana: int = 20

        enemies = battlefield[:]

        sorted_hand = sorted(hand, key=lambda card: card.cost)
        for card in sorted_hand:
            if card.cost > available_mana:
                print("You Do Not Have Enough Mana💧")
                return

            cards_played.append(card)
            mana_used += card.cost
            available_mana -= card.cost

            if isinstance(card, CreatureCard):
                if enemies:
                    target = enemies[0]
                    card.attack(target)
                    damage_dealt += card.attack
                    targets_attacked.append(target.name)
                else:
                    print("No enemies to attack.")
            else:
                print("Your Card Can't Deal Damage.")

        return {
            'cards_played': [card.name for card in cards_played],
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }


    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"


    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(
            available_targets,
            key=lambda target: target.health,
            reverse=True
        )
