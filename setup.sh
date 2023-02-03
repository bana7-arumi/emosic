#!/bin/bash

if [ ! -e "./emotional-analysis-api" ]; then
  git clone --depth=1 https://github.com/Aruminium/emotional-analysis-api
else
  echo "[ERROR] emotional-analysis-api is exist"
fi

cd emotional-analysis-api || exit

./model-install.sh