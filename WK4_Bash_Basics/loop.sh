#!/usr/bin/env sh


echo "#1. seq LAST"
seq 10
echo "#2. seq FIRST LAST"
seq 3 10
echo "#3. seq INCREMENT LAST"
seq 1 3 10
echo "#4. seq -f “FORMAT” FIRST INCREMENT LAST"
seq -f "NO.%01g" 1 5
echo "#5. seq -s “STRING” FIRST INCREMENT LAST"
seq -s " " 2 7
echo "#6 padding with zero"
seq -w 96 101


DURATION=4
COUNT=1
ATTEMPTS=40
PROFILER_SH="/Applications/Docker.app/Contents/MacOS/com.docker.supervisor"
while [ $COUNT -lt $ATTEMPTS ] && [ -n "$(pgrep -f "${PROFILER_SH}")" ]; do
    echo "Waiting ${DURATION} seconds for process ${PROFILER_SH} to complete. This is attempt number $((COUNT))"
    sleep "$DURATION"
    COUNT=$((COUNT+1))
done

echo "Exited the loop"

