from typing import List
from cell import Cell


class Board:
    cells: List[Cell]

    def __init__(self, rows: int = 10, columns: int = 10):
        self.cells = [Cell() for _ in range(rows*columns)]
