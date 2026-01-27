from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict

class EliteCard(Card, Combatable, Magical):

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 defense: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack
        self.defense_power: int = defense
        self.health: int = health


    def play(self, game_state: Dict) -> Dict:

        try:
            if not game_state['is_playable']:
                print("This Card is not playable ❌️")
                return {}
        except Exception:
            print("Error Detected 💣️: game state access fail.")
            return {}

        game_state['available_mana'] -= self.cost
        game_state['battlefield'].append(self)

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Elite Card summoned to battlefield"
        }


    def attack(self, target) -> Dict:
        if self.attack_power <= 0:
            print("Error: You can't deal damage")
            return {}
        elif self.health <= 0:
            print("Error: Already Dead 💀!")
            return {}
        if not isinstance(target, Combatable):
            print("Error: The card must be a Combatable card")
            return {}
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack_power,
            'combat_type': 'melee'
            }


    def defend(self, incoming_damage: int) -> Dict:
        if self.health <= 0:
            print("Error: Your Card is already dead ☠️")
            return {}
        if incoming_damage <= 0:
            print("Error: Invalid incoming damage provided ❌️")
            return {}

        damage_taken = max(0, incoming_damage - self.defense_power)
        self.health -= damage_taken

        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.defense_power,
            'still_alive': self.health > 0
        }


    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        if not targets:
            print("Error: There are no to targets !")
            return {}
        if self.health <= 0:
            print("Error: You Card is already Dead ☠️")
            return {}
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 4,
        }


    def channel_mana(self, amount: int) -> Dict:
        current_mana = 4

        if amount <= 0:
            print("Error: Invalid mana amount ❌️")
            return {}

        if self.health <= 0:
            print("Error: Cannot channel mana while dead ☠️")
            return {}

        return {
            'channeled': amount,
            'total_mana': current_mana + amount,
            }


    def get_combat_stats(self) -> Dict:
        return {
            'attack': self.attack_power,
            'defense': self.defense_power,
            'current_health': self.health,
            'combat_style': 'melee'
        }


    def get_magic_stats(self) -> Dict:
        return {
            'can_cast_spells': True,
            'mana_channeling': True,
            'magic_type': 'elite'
        }
