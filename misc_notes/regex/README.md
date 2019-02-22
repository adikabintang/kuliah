Tutorial: https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285

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
...