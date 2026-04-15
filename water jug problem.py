from collections import deque

def water_jug(m, n, d):
    visited = set()
    queue = deque()
    
    # initial state
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        # skip if already visited
        if (x, y) in visited:
            continue
        
        print(f"({x}, {y})")
        visited.add((x, y))
        
        # check target
        if x == d or y == d:
            print("Target reached!")
            return
        
        # possible operations
        
        # 1. Fill Jug1
        queue.append((m, y))
        
        # 2. Fill Jug2
        queue.append((x, n))
        
        # 3. Empty Jug1
        queue.append((0, y))
        
        # 4. Empty Jug2
        queue.append((x, 0))
        
        # 5. Pour Jug1 -> Jug2
        transfer = min(x, n - y)
        queue.append((x - transfer, y + transfer))
        
        # 6. Pour Jug2 -> Jug1
        transfer = min(y, m - x)
        queue.append((x + transfer, y - transfer))
    
    print("No solution")
    

# Example
water_jug(4, 3, 2)
