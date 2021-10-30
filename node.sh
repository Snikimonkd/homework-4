#!/usr/bin/env bash

if [ `uname` = "Linux" ]; then
    java -Dwebdriver.chrome.driver="./chromedriver" \
        -Dwebdriver.gecko.driver="./geckodriver" \
        -jar selenium-server-standalone-3.141.59.jar \
        -role node \
        -hub http://127.0.0.1:4444/grid/register \
        -browser browserName=chrome,maxInstances=2 \
        -browser browserName=firefox,maxInstances=2
elif [ `uname` = "Darwin" ]; then
    java -Dwebdriver.chrome.driver="./chromedriver-mac" \
        -Dwebdriver.gecko.driver="./geckodriver-mac" \
        -jar selenium-server-standalone-3.141.59.jar \
        -role node \
        -hub http://127.0.0.1:4444/grid/register \
        -browser browserName=chrome,maxInstances=2 \
        -browser browserName=firefox,maxInstances=2
else 
    echo "Unknown OS"
fi