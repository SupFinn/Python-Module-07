from ex0.Card import Card
from typing import List

class AggressiveStrategy:
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards: List[Card]= []
        mana_used: int = 0
        damage_dealt: int = 0
        


    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"


    def prioritize_targets(self, available_targets: list) -> list:
        pass