import random
from dataclasses import dataclass
from enum import Enum


@dataclass
class MazeLocation:
    row: int
    column: int


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


class Maze:

    def __init__(self, cols=10, rows=10, start=MazeLocation(0, 0), goal=MazeLocation(9, 9),
                 sparseness=0.2):
        self._cols = cols
        self._rows = rows
        self._start = start
        self._goal = goal
        self._sparseness = sparseness
        self._maze = [[Cell.EMPTY for _ in range(self._rows)] for _ in range(self._cols)]
        self.fill_randomly()
        self._maze[start.row][start.column] = Cell.START
        self._maze[goal.row][goal.column] = Cell.GOAL

    def fill_randomly(self):
        for r in range(self._rows):
            for c in range(self._cols):
                if random.uniform(0, 1.0) <= 0.2:
                    self._maze[r][c] = Cell.BLOCKED

    def __repr__(self):
        output = ''
        for row in self._maze:
            output = '\n'.join([output, (' '.join(c.value for c in row))])
        return output


maze = Maze()
print(maze)
