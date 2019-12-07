#!/usr/bin/env bash

echo " ------------- Replace -------------- "
echo "#1"
# replace Nick with John
sed 's/Nick/John/g' report.txt

echo "#2"
# Replace Nick with John except for the 2nd line
sed '2!s/Nick/John/' report.txt

echo "#3"
# Replace foo with bar only for the first instance in a line.
sed 's/foo/bar/' report.txt

echo "#4"
# Replace foo with bar only for the 4th instance in a line.
sed 's/foo/bar/2' report.txt

echo "#5"
# Replace foo with bar only for all instances in a line.
sed 's/foo/bar/g' report.txt

echo "#6"
# replace Nick and nick with John between line 3 to 5.
sed '3,5 s/[Nn]ick/John/g' report.txt



echo " ------------- Add -------------- "
echo "#1"
# Add space to the left of a text for pretty printing.
sed 's/^/ /' report.txt

echo "#2"
# Double space the file
sed G report.txt

echo "#3"
# Triple space the file
sed 'G;G' report.txt


echo " ------------- Show -------------- "
echo "#1"
# Display only one paragraph, starting with No one and ending with lives
sed -n '/^No one/,/lives/p' report.txt

echo "#2"
# Only take the 2nd and the 3rd line.
sed -n 2,3p report.txt

echo "#3"
# Exclude the 2nd and the 3rd line
sed 2,3d report.txt

echo "#4"
# Print only the first match of; RE (regular expression)
sed -n '/nick/{p;q;}' report.txt


echo " -------------------- Delete ----------------------"
echo "#1"
# Delete the last line
sed '$d' report.txt

echo "#2"
# Delete the 6th line
sed '6d' report.txt

echo "#3"
# Delete line from 3 to 6
sed '3,6d' report.txt

echo "#4"
# Delete pattern matching line
sed '/nic*/d' report.txt

echo "#5"
# Delete all spaces in front of every line of file.txt
sed 's/^[ ^t]*//' report.txt

