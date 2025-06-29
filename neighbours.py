from screen import Screen as sc


class Neighbours:
    def get_neighbours(position):
        x, y = position
        neighbours = []
        for dx in [-1, 0, 1]:
            if x + dx < 0 or x + dx > sc.GRID_WIDTH:
                continue
            for dy in [-1, 0, 1]:
                if y + dy < 0 or y + dy > sc.GRID_HEIGHT:
                    continue
                if dx == 0 and dy == 0:
                    continue

                neighbours.append((x + dx, y + dy))
        
        return neighbours