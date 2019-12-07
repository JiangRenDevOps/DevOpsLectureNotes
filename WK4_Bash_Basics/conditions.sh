#!/usr/bin/env bash
# #!/bin/sh
# https://www.shellcheck.net/
var=""
## Syntax 1 ##
if [[ -z "$var" ]]; then
    # ^-- SC2039: In POSIX sh, [[ ]] is undefined.
    echo "Empty $var"
else
    echo "Do whatever you want as \$variable is not empty"
fi

## Syntax 2 ##
[[ -z "$var" ]] && echo "Empty" || echo "Not empty"

## Syntax 3 ##
[  -z "$var" ] && echo "Empty: Yes" || echo "Empty: No"

## Syntax 4 ##
# Always keep spaces between the brackets and the actual check/comparison
# Always terminate the line before putting a new keyword like “then”
if (( $1 )); then
    if [ $1 -gt 100 ]
    then
        echo Hey that\'s a large number.
        if (( $1 % 2 == 0 )); then
            echo And is also an even number.
        fi
    fi
fi

var=-5
# Examine if the variable is a number
if [[ $var =~ ^-?[0-9]+$ ]]; then
    # The ^ indicates the beginning of the input pattern
    # The - is a literal "-"
    # The ? means "0 or 1 of the preceding (-)"
    # The + means "1 or more of the preceding ([0-9])"
    # The $ indicates the end of the input pattern
    echo $var is a number
fi

var="String"
# Examine if the variable contain any string
if [[ ! -z $var ]]; then
    echo $var is a non-empty string
fi

if [[ -n $var ]]; then
    echo $var is again a non-empty string
fi

if [ -n $var ]; then
    echo $var is again and again a non-empty string
fi

