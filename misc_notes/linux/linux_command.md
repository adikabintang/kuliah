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

## read
read input.

Example:
```bash
read varname
echo "Hello $varname"
```

## cut
https://www.thegeekstuff.com/2013/06/cut-command-examples/

`cut -c2 test.txt`  print (like `cat`) but only the 2nd character from each line of the test.txt.

`cut -c1-3 test.txt` print character 1 to 3 (like `asu`, 3 character from the first character) from each line of the test.txt.

`cut -c3- test.txt` print from the 3rd character.

`cut -c-8 test.txt` print from the first to the 8th character from each line of the test.txt.

`cut -c- test.txt` same as `cat test.txt`.

`cut -d':' -f1 /etc/passwd`   -d is delimiter, -f is the field. in this case, the output would be something like:
```
root
bin
sync
nginx
```

## xargs
...

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

# Loop, Conditional, etc
## Loops
Example 1:
```bash
for i in {1..4}
do
    echo "$i"
done

# output:
# 1
# 2
# 3
# 4
```

Example 2:
```bash
for i in {0..4..2}
do 
    echo "$i"
done

# output
# 0
# 2
# 4
```

Example 3:
```bash
for file in server.cpp plain.zip
do
	wc $file
done

# output:
# 19  49 484 server.cpp
# 143900   815790 44879792 plain.zip
```

## Conditional
Example 1:
```bash
var="kancut"
if [ "$var" = "abc" ]; then
    echo "true"
else
    echo "false"
fi
```

Example 2:
```bash
x=0
y=1
if [ "$x" -eq "$y" ]; then
    echo "x is equal to y"
elif [ "$x" -gt "$y" ]; then
    echo "x is greater than y"
elif [ "$x" -lt "$y" ]; then
    echo "x is less than y"
fi

if [ "$x" -ne "$y" ]; then
    echo "x is not equal to y"
fi
```

Example 3:
```bash
name="jeff beck"
# check if it's an empty string
if [ -z "$name" ]; then
    echo "name is an empty string"
fi

# check if the length is not zero
if [ "$name" ]; then
    echo "name's length is NOT zero"
fi
```

Example 4:
```bash
file_1="server.cpp"
file_2="one.cpp"
dir_1="cpp"
dir_2="catch2"

if [ -f "$file_1" ]; then
	echo "$file_1 exists"
fi

if [ -f "$file_2" ]; then
        echo "$file_2 exists"
fi

if [ -d "$dir_1" ]; then
        echo "$dir_1 exists"
fi

if [ -d "$dir_2" ]; then
        echo "$dir_2 exists"
fi
```

`-f` and `-d` do not work recursively (i.e. they do not look inside other directories).

For other than `-f` and `-d`,  see: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html 

## Arithmethic Operations
Example:
```bash
x=2
y=9
echo `expr "$x" + "$y"`
echo `expr "$x" - "$y"`
echo `expr "$x" \* "$y"`
echo `expr "$x" / "$y"`
```

## Get return status of last executed command
Syntax: `?`

Example:
```bash
ls # assume ls runs successfully 
echo $? # print 0 (return value of success status)
```

## to uppercase and to lowercase
Example:
```bash
var="aLaY"
echo ${var,,} # to lowercase
echo ${var^^} # to uppercase
```