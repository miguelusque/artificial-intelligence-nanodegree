#!/bin/sh

#NOW=$(date +"%y-%m-%d %H:%M:%S")
sleep 3600
for i in `seq 1 20`;
        do
			NOW='aggresive_chaser_'$(date +"%y-%m-%d_%H.%M.%S")'.txt'
			python tournament.py > $NOW
			sleep 400
        done    
