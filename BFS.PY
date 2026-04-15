Create an empty queue Q
Create a visited array/set and mark all nodes as not visited
Mark the starting node s as visited
Insert s into the queue Q
While Q is not empty, repeat:
Remove (dequeue) a node u from Q
Visit/print node u
For each neighbor v of node u:
If v is not visited:
Mark v as visited
Insert v into Q
End
