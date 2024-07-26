

def min_steps_to_target(N, knightPos, targetPos):

    from collections import deque

    def is_within_bounds(x, y, N):
        return 1 <= x <= N and 1 <= y <= N

    # Possible moves for a Knight
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    # Queue for BFS with initial position and step count
    queue = deque([(knightPos[0], knightPos[1], 0)])
    
    # Visited set to keep track of visited positions
    visited = set((knightPos[0], knightPos[1]))
    
    while queue:
        x, y, steps = queue.popleft()
        
        # If we reach the target position
        if (x, y) == (targetPos[0], targetPos[1]):
            return steps
        
        # Explore all possible moves
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            if is_within_bounds(nx, ny, N) and (nx, ny) not in visited:
                print("nx,ny: ({},{})".format(nx,ny))
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    # If the target position is not reachable
    return -1

# Example usage
N = 6
knightPos = [4, 5]
targetPos = [1, 1]
print(min_steps_to_target(N, knightPos, targetPos))  # Output: 3
