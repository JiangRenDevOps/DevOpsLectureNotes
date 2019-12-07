#!/usr/bin/env bash

echo "Tutorial 1. filter the directory hierarchy based on a file’s name"

echo "-----------------locate-----------------"
# Locate the file. But this require the database for files to be built first
echo "#1. Locate all jpg files"
locate *.jpg

echo "#2. Ignore case sensitivity"
locate -i *.jpg

echo "-----------------find-------------------"
echo "Syntax: find (options) starting/path expression"

echo "#1 Find a file called testfile.txt in current and sub-directories."
find . -name report.txt

echo "#2 Find all .jpg files in the /home and sub-directories."
find /home -name *.jpg

echo "#3 Find an empty file within the current directory"
find . -type f -empty

echo "#4 Find all .db files (ignoring text case) modified in the last 7 days by a user named vagrant."
find /home -user vagrant -mtime 7 -iname ".db"

echo "#5 This command enables the maximum optimization level (-O3) and allows find to follow symbolic links (-L). find searches the entire directory tree beneath /var/www/ for files that end with .html."
find -O3 -L /var/www/ -name "*.html"

echo "(Home work) Try to figure out what this mean: "
find . -type f -exec grep "example" '{}' \; -print

echo "#6 Be careful!!!Add the option -delete to the end of a match expression to delete all files that match."
find . -name "*.pyc" -delete

echo "Tutorial 2. search based on the content of the file"
echo "-----------------grep-------------------"
echo "#1 Let us grep all the occurrence of contents that contain 'find' in the current folder"
grep -i -r "find" .

echo "#2 Of course, you can search for the word 'find' in a length file"
grep find search.sh

echo "#3 filter a length output from the previous output"
ls /usr/lib | grep "xml"

echo "#4 what processes do docker run?"
ps aux | grep docker

echo "#5 let us checkout the command history and find out how did we use bash"
history | grep "bash"


