'''
    Name: Rishabh Mathur
    Date: 14 June, 2024
'''

from collections import deque

def topological_sort(v, adj):
    # Step 1: Calculate in-degrees
    indegree = [0] * v
    for i in range(v):
        for it in adj[i]:
            indegree[it] += 1
    
    # Step 2: Initialize the queue with vertices having in-degree 0
    q = deque()
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)
    
    ans = []  # This list will store the topological order
    
    # Step 3: Process the queue
    while q:
        f = q.popleft()
        ans.append(f)
        for it in adj[f]:
            indegree[it] -= 1  # Reduce in-degree by 1
            if indegree[it] == 0:
                q.append(it)
    
    # Step 4: Check for cycles
    return len(ans) != v  # If len(ans) != v, there's a cycle

# Example usage:
v = 6
adj = [
    [2, 3],  # edges from vertex 0
    [3, 4],  # edges from vertex 1
    [3],     # edges from vertex 2
    [5],     # edges from vertex 3
    [5],     # edges from vertex 4
    []       # edges from vertex 5
]

# Check for cycles
has_cycle = topological_sort(v, adj)
if has_cycle:
    print("The graph has a cycle.")
else:
    print("The graph does not have a cycle.")
