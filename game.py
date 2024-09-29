from collections import deque
import random
from typing import List
from board import Board
from dice import Dice
from player import Player


class Game:
    board: Board
    dice: Dice
    players: deque[Player]
    total_cells : int

    def __init__(self, player_count:int = 2, snake:int=5, ladder:int=5):
        self.total_cells = 100
        self.board = Board(rows=10, columns=10)
        self.dice = Dice()
        self.players = deque()
        for i in range(player_count):
            self.players.append(Player(i+1))

        while snake:
            first = random.randint(0, self.total_cells-1)
            second = random.randint(0, self.total_cells-1)

            if first < second:
                first, second = second, first
            self.board.cells[first].addJump(first, second)

            snake -= 1
        
        while ladder:
            first = random.randint(0, self.total_cells-1)
            second = random.randint(0, self.total_cells-1)

            if first > second:
                first, second = second, first
            self.board.cells[first].addJump(first, second)

            ladder -= 1

    def start(self):
        while(True):
            curr_player = self.players.popleft()

            dice_value = self.dice.rollDice()
            print(f"Player{curr_player.player_id+1} dice rolled: {dice_value}")

            total_dice_value = sum(dice_value)
            if curr_player.curr_pos + total_dice_value < self.total_cells:
                curr_player.curr_pos += total_dice_value
            
            
            cell_jump = self.board.cells[curr_player.curr_pos].jump
            if cell_jump:
                if cell_jump.start > cell_jump.end:
                    print(f"Snake found")
                if cell_jump.start < cell_jump.end:
                    print(f"Ladder found")
                curr_player.curr_pos = cell_jump.end
                    
            print(f"Player{curr_player.player_id} final position is: {curr_player.curr_pos+1}")
            if curr_player.curr_pos+1 == self.total_cells:
                print(f"Player{curr_player.player_id} Won!!!")
                break

            self.players.append(curr_player)


