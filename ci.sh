#!/bin/bash -ex

if [[ "x$PHASE" != "x" ]]; then
  if [[ "$PHASE" == "SUITE_BASIC" ]]; then
    echo "Run some basic selenium tests!"
    ./build.sh
    exit 0
  elif [[ "$PHASE" == "SUITE_ADVANCED" ]]; then
    echo "run advanced test suite"
    exit 0
  else
    echo "**** Error PHASE value is unexpected"
    exit 1
  fi
else
  echo "****** Error Phase is not set"
fi

