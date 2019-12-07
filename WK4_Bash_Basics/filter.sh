#!/usr/bin/env bash

ls -l | awk '{print $9}' | uniq -c | sort

ls -l | awk '{print $9"\t"$1}'

ls -l | awk '
BEGIN { print "File\tOwner" }
{ print $9, "\t", $3}
END { print " - DONE -" }
'

#
# -F fs     To specify a file separator.
#
# -f file     To specify a file that contains awk script.
#
# -v var=value     To declare a variable.
#

# Sometimes the separator in some files is not space nor tab but something else. You can specify it using –F option:

awk -F: '{print $1}' /etc/passwd


# Replace
echo "Hello Tom" | awk '{$2="Adam"; print $0}'

ls -l | awk '{$3="Yu Wang"; print $0}'