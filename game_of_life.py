world = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]
        ]

world_len = len(world)

def count_neighbors(row,col):
    neighbors = 0
    if col > 0:
        # left neighbor
        neighbors += world[row][col-1]
    if col < world_len-1:
        # right neighbor
        neighbors += world[row][col+1]
    if row > 0:
        # up neighbor
        neighbors += world[row-1][col]
    if row < world_len-1:
        # down neighbor
        neighbors += world[row+1][col]

    return neighbors


def future_state(row, col):
    neighbors = count_neighbors(row, col)
    state = world[row][col]
    print(f"cell:{row, col} neighbors:{neighbors}")
    if state == 1:
        # Any live cell with fewer than two live neighbors dies, as if caused by under population.
        if neighbors < 2:
            state = 0
        # Any live cell with two or three live neighbors lives on to the next generation.
        if neighbors == 2 | neighbors == 3:
            state = 1
        # Any live cell with more than three live neighbors dies, as if by overcrowding.
        if neighbors > 3:
            state = 0
    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    elif state == 0 & neighbors == 3:
        state = 1
            
    return state

def all_dead(world):
    row_status = []
    for row in world:
        row_status.append(all(row) == False)
    return all(row_status) == False

def game_of_life(world):
    next_gen = world.copy()
    world_len = len(world)
    for col in range(world_len-1):
        for row in range(world_len-1):
            next_gen[row][col] = future_state(row, col)

    return next_gen


# print(game_of_life(world))

