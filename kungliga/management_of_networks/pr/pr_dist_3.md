Name: Adika Bintang Sulaeman

---

# Part A: send update of partial aggregate to parent only

## Properties of object aggregator function related to the task

As shown on the slide from the class, the `aggregate()` function works as the following:

```
Aggregator object A
    procedure aggregate()
        self_aggregate = self_aggregate \
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

# Part B: 