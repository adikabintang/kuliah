# Really Basics
## file
`file` find out type of files.
example
```bash
$ file test.xt
> test.txt: ASCII text
```

## find
find files. Example:
```
find -type f -name main.c      ( f for files, d for dir )
```

## locate
like files, but not search in the filesystem. it looks to updatedb. pros: faster than `find`. cons: not as consistent as `find`, especially when there is a change in the filesystem.
example:
```
locate main.c (will look every file containing main.c, like `grep main.c`)
```

## du
check file/dir size.
example:
```
$ du -h file.txt (-h to make it readable like 4.0K, 46M, etc)
$ du -h foldername (will print the size recursively)
$ du -h foldername -d 0 (-d for depth, 0 will print the size of foldername only)
$ du -h foldername -d 1 (will print -d 0 and the recursive of depth 1)
```
## df
show disk usage
## sort
example
```bash
$ cat file.txt
b
c
a

$ sort file.txt
a
b
c

$ sort -r file.txt
c
b
a
```

## wc
word count
line counting
byte counting

## uptime
tells how long the system has been running.

## whatis
display one-line manual page description of a command. example
```
$ whatis whatis
whatis (1)           - display one-line manual page descriptions

$ whatis tee
tee (1)              - read from standard input and write to standard output and files
tee (1p)             - duplicate standard input
tee (2)              - duplicating pipe content
```

## tee
Read from standard input and write to standard output and files. For example, if we use `ping google.com > file.txt`,  the output will be in file.txt but not in stdout. But with tee, we can get both to stdout and file.txt. Example:
```
$ ping google.com | tee file.txt

or we can even output to multiple files

$ ping google.com | tee file.txt another.txt
```

## sed
sed: stream editor for filtering and transforming text. 

Example 1 replacing string, [link](https://unix.stackexchange.com/questions/159367/using-sed-to-find-and-replace):
```
sed -i -e 's/before/after/g' hello.txt
```

## awk
pattern scanning and processing language. huh?

Example 1, printing column of a text [link](https://www.tutorialspoint.com/awk/awk_basic_examples.htm):
```
$ cat file.txt
1) Amit     Physics   80
2) Rahul    Maths     90

$ awk '{print $1}' file.txt
1)
2)

$ awk '{print $2 " " $4}' file.txt
Amit 80
Rahul 90

# print line which has more than 18 chars
$ awk 'length($0) > 18' file.txt
```

# Basic Networking
## traceroute
print the route packets trace to network host.
Example:
```
$ traceroute google.com
```

## dig
DNS lookup utility. Example:
```
$ dig geekflare.com
```

## telnet.
user interface to the TELNET protocol. used to check if the connection is ok. example:
```
telnet geekflare 443
```

## netstat
Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

Review network connection and open sockets.

## nmap
check opened ports. port scanner.