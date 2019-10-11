Name: Adika Bintang Sulaeman

---

# Part A: send update of partial aggregate to parent only

## Properties of object aggregator function related to the task

As shown on the slide from the class, the `aggregate()` function works as the following:

```
Aggregator object A
    procedure aggregate()
        self_aggregate = local_variable \
            + sum(aggregate values of the chilren)
        
        return self_aggregate 
```

This means that the change in the partial message only happens when an update was given from the child. Therefore, the proposed solution is to give a flag for changes from the child (`LOCALVAR` or `UPDATE`), then send `UPDATE` to the parent.

```
procedure GAP()
    T := empty table;
    if v == root then
        addEntry(root, parent, -1, undef);
        addEntry(root, self, 0, undef);
    else
        addEntry(v, self, undef, undef);
    
    vector := updateVector();
    send(UPDATE, v, vector) to all neighbors;
    A.initiate();
    while true do
        from_child := false;

        read message;
        switch (message)
            case (NEW, from):
                addEntry(from, peer, undef, undef)
                send(UPDATE, v, vector) to from;
            case (FAIL, from):
                removeEntry(from);
            
            // The message LOCALVAR indicates 
            // a change in local variable.
            case (LOCALVAR, x):
                from_child := true;
            
            case (UPDATE, from, level, parent, aggregate):
                updateEntry(from, level, parent, aggregate);
                
                // check if the UPDATE message 
                // comes from the child
                if level > vector.level:
                    from_child := true;
        end switch

        restoreTableInvariant();
        A.aggregate();
        if v == root then
            A.global();
        
        newVector = updateVector();
        if newVector != vector then
            vector := newVector;

            if from_child == true then
                send (UPDATE, v, newVector) to vector.parent;
            else
                send (UPDATE, v, newVector) to all neighbors;
```

# Part B: Send an update if abs(new aggregate - previous agrregate) > b

```
procedure GAP()
    var b: integer;
    T := empty table;
    if v == root then
        addEntry(root, parent, -1, undef);
        addEntry(root, self, 0, undef);
    else
        addEntry(v, self, undef, undef);
    
    vector := updateVector();
    send(UPDATE, v, vector) to all neighbors;
    A.initiate();
    while true do
        from_child := false;

        read message;
        switch (message)
            case (NEW, from):
                addEntry(from, peer, undef, undef)
                send(UPDATE, v, vector) to from;
            case (FAIL, from):
                removeEntry(from);
            
            // The message LOCALVAR indicates 
            // a change in local variable.
            case (LOCALVAR, x):
                from_child := true;
            
            case (UPDATE, from, level, parent, aggregate):
                updateEntry(from, level, parent, aggregate);
                
                // check if the UPDATE message 
                // comes from the child
                if level > vector.level:
                    from_child := true;
        end switch

        restoreTableInvariant();
        A.aggregate();
        if v == root then
            A.global();
        
        newVector = updateVector();
        if newVector != vector:
            if |newVector.aggregate - vector.aggregate| > b:
                if from_child == true then
                    send (UPDATE, v, newVector) to \
                        vector.parent;                    

            vector := newVector;
            if from_child == false then
                send (UPDATE, v, newVector) to all neighbors;
```

Let's say we have the budget `b = 10` for a binary tree-like network with height 5. First of all, the definition of the local aggregate is `local aggregate = local variable + sum(aggregate of child)`. This means that if we put a threshold `b` to decide where to send, as long as the local variable change on the node is greater than `b`, the report will be reported up to the root node for global aggregate because the absolute difference of the previous aggregate to the current aggregate will also greater than `b`. In other words, the value of error budget `b` will determine how the implementor of the system tolerate the accuracy and the height of the tree does not affect the accuracy.