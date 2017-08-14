#!/bin/bash -e
export DISPLAY=:1
export PATH=/firefox:$PATH

echo $PATH
echo $DISPLAY

ps -aux

echo "Running selenium tests"
python main.py

