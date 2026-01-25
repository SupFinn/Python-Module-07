from ex0.Card import Card
from typing import Dict

class CreatureCard(Card):

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health


    def play(self, game_state: dict) -> Dict:
        try:
            if not game_state['is_playable']:
                print("This Card is not playable ❌️")
                return {}
            if game_state['available_mana'] < self.cost:
                print("MANA: too low mana!")
                return {}
        except Exception:
            print(f"Error Detected: game state access fail.")
            return {}

        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self)

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }


    def get_card_info(self) -> Dict:
        stats: Dict = super().get_card_info()
        stats.update({
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        })
        return stats


    def attack_target(self, target) -> Dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }