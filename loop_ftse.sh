#!/bin/bash
START=$(date +"%H:%M:%S %d/%m") # Get start time/date *european date format*

while true
do
    BEGIN=$(($(date +%s%N)/1000000))
    python get_ftse.py $2
    echo "Script has been running since $START"
    END=$(($(date +%s%N)/1000000))
    WAIT=$(( (END-BEGIN) / 1000))
    sleep $(($1-WAIT))
done

