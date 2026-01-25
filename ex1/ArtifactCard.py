from ex0.Card import Card
from typing import Dict

class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect


    def play(self, game_state: Dict) -> Dict:
        try:
            if not game_state['is_playable']:
                print("This Card is not playable ❌️")
                return {}
            if game_state['available_mana'] < self.cost:
                print("MANA: too low mana!")
                return {}
            if self.durability <= 0:
                print("Your Card Got Exhausted Already ☠️.")
                return {}
        except Exception:
            print(f"Error Detected 💣️: game state access fail.")
            return {}


        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self)

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }


    def activate_ability(self) -> Dict:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "reason": "Artifact exhausted"
            }

        self.durability -= 1

        return {
            "artifact": self.name,
            "activated": True,
            "effect": self.effect,
            "durability_left": self.durability
        }