Tutorial: https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285

For testing: https://regex101.com/r/cO8lqs/11 

# Basic

## Anchors: ^ and $
### ^start
`^something` -> matches string **starting** with "something".

Example
```
^asu
will select "asu" in
asu koe mangan rumput
```

### end$
`lastword$` -> matches string **ending** with "lastword".

Example:
```
govan$
will match "govan" in
guthrie govan

but not in
guthrie govan plays the guitar
```

### ^exact_match$
`^exact$` -> exact string match

### matches that contains "word"
Example
```
eek

will match
oi eek lu bau
```

## Quantifiers: * + ? and {}

`abc*`   matches a string that has **ab followed by 0 or more c**

`abc+`   matches a string that has **ab followed by 1 or more c**

`abc?`   matches a string that has **ab followed by 0 or 1 c**

`abc{2}`   matches a string that has **ab followed by 2 c**

`abc{2,}`  matches a string that has **ab followed by 2 or more c**

`abc{2,5}` matches a string that has **ab followed by 2 up to 5 c**

`a(bc)*`   matches a string that has **a followed by 0 or more copies of bc**

`a(bc){2,5}` matches a string that has **a followed by 2 up to 5 copies of bc**

## OR operator: | and []

`a(b|c)`   matches a string that has **a followed by b or c**

`a[bc]`    same as `a(b|c)`

## Character classes: \d, \w, \s, and . (read: dot)

`\d`   matches a **single digit**. for example, it will match 2, 4, 2 in "aob a2b a42c" (see, it matches a *single* digit). Negation: `\D` (matches a single non-digit character)

`\w`   matches a **word character (alphanumeric and _)**. Negation: `\W` (matches a non-word character)

`\s`   matches a **space** (including tabs and line breaks). Negation: `\S`

`.`    matches any character

## How to escape the character
using `\`. For example, to match the character `$` in a string, we would use `\$`.

## Flags
A regex usually comes with the form like `/abc/`, where the search pattern is delimited by two `/` characters. At the and of `/` we can specify a flag with these values:
- **i** (case insensitive) for example, `/aBc/` would match `Abc`
- **g** (global) does not return after the first match, restarting the subsequent searches from the end of the previous match
- **m** (multi-line) when enabled `^` and `$` will match the start and end of a line, instead of the whole string.  

# Intermediate 
## Grouping and capturing

`a(bc)`   paretheses create a **capturing group with value bc**

What?? The point is, *it creates grouping*.

For example, `a(bc)(op)`: 
- mathces character `a`
- 1st capturing group: matches character `bc`
- 2nd capturing group: matches character `op`

Explanation with example:
```
regex: a(bc)
string: abc bca abcd ab abcop
result:
match 1
full match (group 0): abc (pos: 0-3)
group 1: bc (pos: 1-3)

match 2
full match (group 0): abc (pos: 8-11 or see abc in abcd)
group 1: bc (pos: 9-11)

match 3
full match (group 0): abc (pos: 16-19 or see abc in abcdop)
group 1: bc (pos: 17-19)

------------------------------
regex: a(bc)op
string: abc bca abcd ab abcop
result:
match 1
full match (group 0): abcop
group 1: bc  (in abcop)

------------------------------
regex: a(bc)(op)
string: abc bca abcd ab abcop
result:
match 1
full match (group 0): abcop
group 1: bc
group 2: op
```

`a(?:bc)*`   using `?:` we **disable the capturing group**. `:?` is called *non-capturing group*.

Example:
```
string: abc ac acb aob a2b a42c A87d

regex: a(?:bc)
result:
full match: abc

regex: a(?:bc)*
full match: abc
full match: a
full match: a
full match: a
full match: a
full match: a
why? because * means matches between 0 and unlimited times bc
```

`a(?<foo>bc)` using `?<foo>` we put a name to the group.
Example:
```
string: abc ac acb aob a2b a42c A87d
regex: a(?<foo>bc)
result:
full match: abc
Group `foo`: bc
```

## Bracket expressions
Inside bracket `[]`, special characters lose their power and we will not apply the escape character rule.

`[abc]`   matches a string that has **either a or b or c** (same as `a|b|c`).

`[a-c]`   same as previous

Example:
```
string: abc ac acb aob
regex: [abc]
result:
match 1: a
match 2: b
match 3: c
match 4: a
match 5: c
match 6: a
match 7: c
match 8: b
match 9: a
match 10: b
```

`[a-fA-F-0-9]`  matches a string that represents a single hexadecimal digit, case insensitively.

`[0-9]%`   matches a string that has a character from 0 to 9 before % sign.

`[^a-zA-Z]`  a string that has **not a letter from a to z or from A to Z**. In this case the ^ is used as a **negation of the expression**.
Example:
```
string: sold for $1
regex: [^a-zA-Z]
match 1:  (space)
match 2:  (space)
match 3: $
match 4: 1
```

## Greedy and Lazy match
The quantifiers `* + {}` are greedy operators, so they expand the match as far as they can through the provided text.

For example, 
```
string: This is a <div> simple div</div> test
regex: <.+>
match: <div>simple div</div>
```

To make it lazy, we use `?`. For instance,
`<.+?>`  matches any character one or more times inclyded inside <>, expanding as needed. For example:
```
string: This is a <div> simple div</div> test
regex: <.+?>
match 1: <div>
match 2: </div>

string: This is<> a <div> simple div</div> test
regex: <.+?>
match 1: <> a <div>
match 2: </div>
```

To get a stricter regex matches tag inside <>, we can use:

`<[^<>]+>` matches at least one character inside <> except (except symbol: ^) the character < or >. Example:
```
string: This is<> a <div> simple div</div> test
regex: <.+?>
match 1: <div>
match 2: </div>
```


