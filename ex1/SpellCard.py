from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type


    def play(self, game_state: dict) -> dict:
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
            'effect': self.effect_type
        }


    def resolve_effect(self, targets: list) -> dict:
        return {
            'targets': targets,
            'damage': 3,
            'effect': 'damage'
        }