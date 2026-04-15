## BREADTH FIRST SEARCH
CREATE empty queue Q
CREATE empty set Visited

ADD StartNode to Visited
ENQUEUE StartNode into Q

WHILE Q is not empty DO
    CurrentNode ← DEQUEUE Q
    VISIT CurrentNode

    FOR each Neighbor of CurrentNode in Graph DO
        IF Neighbor not in Visited THEN
            ADD Neighbor to Visited
            ENQUEUE Neighbor into Q
        END IF
    END FOR
END WHILE

## DEPTH FIRST SEARCH
CREATE empty set Visited

PROCEDURE DFS(Node)
    IF Node not in Visited THEN
        VISIT Node
        ADD Node to Visited

        FOR each Neighbor of Node in Graph DO
            CALL DFS(Neighbor)
        END FOR
    END IF
END PROCEDURE

CALL DFS(StartNode)
## WATER JUG PROBLEM
CREATE empty queue Q
CREATE empty set Visited

ENQUEUE (0, 0) into Q   // initial state

WHILE Q is not empty DO
    (x, y) ← DEQUEUE Q

    IF (x, y) in Visited THEN
        CONTINUE
    END IF

    ADD (x, y) to Visited
    VISIT (x, y)

    IF x = Target OR y = Target THEN
        PRINT "Solution Found"
        STOP
    END IF

    // Generate next states

    ENQUEUE (Jug1Capacity, y) into Q      // Fill Jug1
    ENQUEUE (x, Jug2Capacity) into Q      // Fill Jug2
    ENQUEUE (0, y) into Q                 // Empty Jug1
    ENQUEUE (x, 0) into Q                 // Empty Jug2

    // Pour Jug1 → Jug2
    transfer ← MIN(x, Jug2Capacity - y)
    ENQUEUE (x - transfer, y + transfer) into Q

    // Pour Jug2 → Jug1
    transfer ← MIN(y, Jug1Capacity - x)
    ENQUEUE (x + transfer, y - transfer) into Q

END WHILE

PRINT "No Solution"
