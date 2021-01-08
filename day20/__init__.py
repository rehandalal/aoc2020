import math
import os

from puzzle import Puzzle


MONSTER_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "monster.txt")

with open(MONSTER_FILE) as f:
    MONSTER = [[char for char in line] for line in f.read().splitlines()]

class P1(Puzzle):
    test_result = 20899048083289

    def parse(self, data):
        data = data.strip("\n").split("\n\n")

        tiles = {}
        for d in data:
            d = d.splitlines()
            tile_id = int(d[0][5:-1])
            tiles[tile_id] = [[c for c in l] for l in d[1:]]
        return tiles

    def rotate(self, tile):
        rotated = [[None] * len(tile) for _ in range(len(tile[0]))]
        for i in range(len(tile[0])):
            for j in range(len(tile)):
                rotated[i][j] = tile[j][-i - 1]
        return rotated

    def flip(self, tile):
        flipped = [[None] * len(tile[0]) for _ in range(len(tile))]
        for i in range(len(tile)):
            for j in range(len(tile[0])):
                flipped[i][j] = tile[i][-j - 1]
        return flipped

    def fits_right(self, a, b):
        for i in range(len(a)):
            if a[i][-1] != b[i][0]:
                return False
        return True

    def fits_below(self, a, b):
        return a[-1] == b[0]

    def search(self, tiles, grid, visited, row=0, col=0):
        for tile_id, tile in tiles:
            if grid[-1][-1] is not None:
                return
            if tile_id in visited:
                continue
            if row > 0 and not self.fits_below(grid[row - 1][col][1], tile):
                continue
            if col > 0 and not self.fits_right(grid[row][col - 1][1], tile):
                continue
            grid[row][col] = (tile_id, tile)
            visited.add(tile_id)
            if col == len(grid) - 1:
                self.search(tiles, grid, visited, row + 1, 0)
            else:
                self.search(tiles, grid, visited, row, col + 1)
            visited.remove(tile_id)

    def answer(self, grid):
        return grid[0][0][0] * grid[0][-1][0] * grid[-1][0][0] * grid[-1][-1][0]

    def pretty_print(self, tile):
        for row in tile:
            print("".join(row))
        print("")

    def solve(self, data):
        tiles = []
        for d in data:
            tile = data[d]
            for i in range(2):
                tile = self.flip(tile)
                for j in range(4):
                    tile = self.rotate(tile)
                    tiles.append((d, tile))
        grid_size = int(math.sqrt(len(data)))
        grid = [[None] * grid_size for _ in range(grid_size)]
        self.search(tiles, grid, set())
        return self.answer(grid)


class P2(P1):
    test_result = 273

    def is_monster(self, grid, row, col):
        for y in range(len(MONSTER)):
            for x in range(len(MONSTER[0])):
                if MONSTER[y][x] == ".":
                    continue
                elif grid[row + y][col + x] not in ("#", "0"):
                    return False
        return True

    def mark_monster(self, grid, row, col):
        for y in range(len(MONSTER)):
            for x in range(len(MONSTER[0])):
                if MONSTER[y][x] == ".":
                    continue
                grid[row + y][col + x] = "0"

    def identify_monsters(self, grid):
        found = False
        for row in range(len(grid) - len(MONSTER)):
            for col in range(len(grid[0]) - len(MONSTER[0])):
                if self.is_monster(grid, row, col):
                    found = True
                    self.mark_monster(grid, row, col)
        return found

    def answer(self, grid):
        assembled_size = len(grid) * (len(grid[0][0][1]) - 2)
        assembled = [[None] * assembled_size for _ in range(assembled_size)]
        for i in range(len(grid)):
            for j in range(len(grid)):
                tile_id, tile = grid[i][j]
                for y in range(8):
                    for x in range(8):
                        assembled[y + (i * 8)][x + (j * 8)] = tile[y + 1][x + 1]

        for i in range(2):
            assembled = self.flip(assembled)
            for j in range(4):
                assembled = self.rotate(assembled)
                identified = self.identify_monsters(assembled)
                if identified:
                    count = 0
                    for row in assembled:
                        for col in row:
                            if col == "#":
                                count += 1
                    return count

