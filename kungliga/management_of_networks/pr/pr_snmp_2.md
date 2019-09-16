1. A function that reads an SNMP table column by column, **one column at the time** (use get-bulk, i.e., the SNMPv2 operation GetBulkRequest)

```C
/*
this is a pseudocode, not a C code:
- some data types are assumed to exist
- the index of an array starts with 1
*/

table_element table [1..n][1..m];
OID table_oid;
int row_max, column_max;

read_table (table_oid, table, &row_max, &column_max) {
    OID oid;
    int number_of_rows = 0, column = 1, row = 1;

    // get the number of the rows
    (oid, value) = get_next(table_oid);

    while (oid is of form [table_oid.1.column.*]) {
        number_of_rows++;
        (oid, value) = get_next(table_oid);
    }

    table[column] = get_bulk(table_oid, number_of_rows);
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

2. Write a function that reads an SNMP table row by row, **one row at the time** (use get-next)

```C
/*
this is a pseudocode, not a C code:
- some data types are assumed to exist
- the index of an array starts with 1
*/

table_element table [1..n][1..m];
OID table_oid;
int row_max, column_max;

read_table (table_oid, table, &row_max, &column_max) {   
    column = 1, row = 1;
    number_of_columns = 0;
    list_of_object_column = []
    list_of_values_in_a_row = []
    list_of_oid_in_a_row = []

    // get the number of columns
    (last_oid_read, value) = get_next(table_oid.1.column)

    // If a GETNEXT is issued on an object that does not exist, 
    // the agent MUST return the next instance in the MIB tree that does exist
    // http://net-snmp.sourceforge.net/wiki/index.php/GETNEXT
    while (last_oid_read is of form [table_oid.1.*]) {
        list_of_object_column.append(table_oid.1.column);
        column++;
        (last_oid_read, value) = get_next(table_oid.1.column);
    }

    column_max = column;
    column = 1;

    // read row by row
    list_of_oid_in_a_row, list_of_values_in_a_row = 
        get_next(list_of_object_column);

    while (list_of_oid_in_a_row[column_max] is of form [table_oid.1.*]) {
        table_elemen[row] = list_of_values_in_a_row;
        row++;
        list_of_oid_in_a_row, list_of_values_in_a_row = 
            get_next(list_of_oid_in_a_row);
    }
    
    row_max = row;
}
```