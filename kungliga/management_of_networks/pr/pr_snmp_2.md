- Name: Adika Bintang Sulaeman
---

## 1. A function that reads an SNMP table column by column, **one column at the time** (use get-bulk, i.e., the SNMPv2 operation GetBulkRequest)

```C
/*
this is a pseudocode, not a real code:
- some data types are assumed to exist
- the index of an array starts with 1
*/

table_element table [1..n][1..m];
OID table_oid;
int row_max, column_max;

read_table (table_oid, table, &row_max, &column_max) {
    OID oid;
    int number_of_rows = 0, column = 1, row = 1;

    // START get the number of the rows
    (oid, value) = get_next(table_oid);

    while (oid is of form [table_oid.1.column.*]) {
        number_of_rows++;
        (oid, value) = get_next(table_oid);
    }
    // END OF get the number of the rows

    // read 1 column using get_bulk
    table[column] = get_bulk(table_oid, number_of_rows);

    // get the OID of the last item in the table column 1
    last_oid_read = table[column][number_of_rows]["OID"];

    while (last_oid_read is of form [table_oid.1.*]) {
        column++;
        table[column] = get_bulk(last_oid_read, number_of_rows);
        last_oid_read = table[column][number_of_rows]["OID"];
    }

    row_max = number_of_rows;
    column_max = column;
}
```

## 2. Write a function that reads an SNMP table row by row, **one row at the time** (use get-next)

```C
/*
this is a pseudocode, not a real code:
- some data types are assumed to exist
- the index of an array starts with 1
*/

table_element table [1..n][1..m];
OID table_oid;
int row_max, column_max;

read_table (table_oid, table, &row_max, &column_max) {   
    column = 1, row = 1;
    number_of_columns = 0;

    // this is a list of  OID of object of the column: such as the OID 
    // of tcpConnState, tcpConnLocalAddress, etc for tcpConnTable
    list_of_object_column = []

    list_of_values_in_a_row = []
    list_of_oid_in_a_row = []

    // START get the number of columns, aggregate column OID in array
    (last_oid_read, value) = get_next(table_oid.1.column)

    // If a GETNEXT is issued on an object that does not exist, 
    // the agent MUST return the next instance in the MIB tree that does exist
    // http://net-snmp.sourceforge.net/wiki/index.php/GETNEXT
    while (last_oid_read is of form [table_oid.1.*]) {
        list_of_object_column.append(table_oid.1.column);
        column++;
        (last_oid_read, value) = get_next(table_oid.1.column);
    }
    // END OF get the number of columns, aggregate column OID in array

    column_max = column;
    column = 1;

    // read row by row
    list_of_oid_in_a_row, list_of_values_in_a_row = 
        get_next(list_of_object_column);

    while (list_of_oid_in_a_row[column_max] is of form [table_oid.1.*]) {
        // assume that we can fill the table row in this operator assignment
        table_element[row] = list_of_values_in_a_row;

        row++;

        // list of OIDs as the parameter
        list_of_oid_in_a_row, list_of_values_in_a_row = 
            get_next(list_of_oid_in_a_row);
    }
    
    row_max = row;
}
```

## 3. Evaluate and compare by examining the number of SNMP operations and SNMP message exchange sizes for:
- The function presented in the class (read element by element)
- Function number 1: read column by column
- Function number 2: read row by row 

### Function 0: read element by element

This function performs `snmp get-next` to read the element of the table one by one. It cannot read multiple `get-next` at the same time because other `get-next` is dependent of the OID returned from the previous `get-next`.

If the table has `m` columns and `n` rows, the number of operation will be `m*n`, which has the complexity of `O(m*n)`. This complexity function also applies to the number of round-trips done with the `snmp get-next`.

Since the document states that we can assume that the SNMP response fits into a single PDU, the size of the response would be `m*n` too. For each response, the message size will be as small as a single message of reading the element of the SNMP table.

### Function 1: read column by column

This function counts the number of rows by performing `snmp get-next` as many as the number of rows. This number of rows is needed as the parameter of `get-bulk` opearation, i.e., to know how many leaves the `get-bulk` needs to read. After obtaining the number of columns, it performs `snmp get-bulk` for each column.

Let's say there are `m` column and `n` rows. The number of operations would be `n+m`, which gives the complexity of `O(n+m)`. Function 1 uses less SNMP operations as well as less round-trip compared to the function 0.

The message size of the response when counting the number of rows is the same as the function 0 because both use `snmp get-next`. However, when reading the column with `get-bulk` operation, the response's size is `m*n*sizeof(one read response)`.

### Function 2: read row by row

This function counts the number of column by performing `snmp get-next` as many as the number of columns. The column OID's objects is aggregated as a list and the list is given as a parameter of the `get-next` operation.

Assuming there is `m` column and `n` rows, counting the number of column will take `m` steps. Reading row by row is done by performing `get-next` with list of OIDs as the parameter, which means it takes `n` operations to read all the rows. The total of the operations is `m+n`, similar to that of the function 1.

The message size when counting the columns is `m*sizeof(one read response)`, and that of when reading from each row is `n*m*sizeof(one read response)`. The message sizes involve in this function also similar to that of function 1.

In conclusion, function 0 (read element by element) takes the most steps, but smaller message size in each response. Function 1 and 2 takes less steps but can have much larger response for some operations compared to that of function 0.