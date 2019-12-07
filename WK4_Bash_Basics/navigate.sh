#!/usr/bin/env bash

echo "#1. print working directory"
pwd

echo "#2. This is ls"
ls

echo "#3. This is ls -l"
ls -l

echo "#4. This is ls -altr"
ls -altr

echo "#5. go to the current folder"
cd .
pwd

echo "#6. go to the parent folder"
cd ../
pwd

echo "#7. go back to the current folder"
cd wk4_bash_basics
pwd

echo "#8. create path to a folder"
mkdir -p ../hello/world/java/
ls -altr ../

echo "#9. rm folders"
rm -r ../hello/world/java/

rm -r ../hello/world/

rm -r ../hello/

echo "#10. Cat a file"
cat report.txt

echo "#11. To view contents of a file preceding with line numbers"
cat -n report.txt

echo "#12. Less: load a file part by part/load file faster"
less report.txt

echo "#12. Dmesg start at first occurrence of pattern “failure” in the file"
dmesg | less -p "failure"
