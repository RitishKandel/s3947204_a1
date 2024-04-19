#!/bin/bash

# Loop through 180 configuration files
for ((i=0; i<=179; i++))
do
    # Run the Python script with the specified arguments
    python3 mazeTester.py "sampleConfig${i}.json"
done
