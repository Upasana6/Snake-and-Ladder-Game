from typing import List


class Player:
    player_id: str
    curr_pos: int

    def __init__(self, id, pos=0) -> None:
        self.player_id = id
        self.curr_pos = pos
