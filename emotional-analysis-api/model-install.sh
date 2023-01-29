#!/bin/bash

function curl_gdrive_download () {
  curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${1}" > /dev/null
  CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
  curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${1}" -o "${2}"
  rm -f ./cookie
}

GDRIVE_MODEL_FILE_ID='18H0SU7xcVxVsTniXbiVBeBJoS62WAoXb'
MODEL_NAME='EmotionAnalysisModel'

FIND_PROJECT=$(find ../emotional-analysis-api/app/)
if [ -z "$FIND_PROJECT" ]; then
  echo "[ERROR] Project 'emotional-analysis-api' is not found."
  exit 1
fi

FIND_MODEL=$(find ../emotional-analysis-api/app/${MODEL_NAME})
if [ -n "$FIND_MODEL" ]; then
  echo "[ERROR] ${MODEL_NAME} is exist"
  exit 1
fi

WHICH_CURL=$(which curl)
if [ -n "$WHICH_CURL" ]; then
  curl_gdrive_download ${GDRIVE_MODEL_FILE_ID} "${MODEL_NAME}.tar.gz"
else
  echo "[ERROR] Could not download."
  echo "Please install curl command"
  exit 1
fi

echo "[SUCCESS] model downloaded!"

if ! tar xvf "./${MODEL_NAME}.tar.gz"; then
  echo "[ERROR] Failed to unzip."
  exit 1
fi

if ! rm "./${MODEL_NAME}.tar.gz"; then
  echo "[ERROR] Failed to delete compressed file."
  exit 1
fi

if ! mv "./${MODEL_NAME}" "./app/${MODEL_NAME}"; then
  echo "[ERROR] Failed to mv ${MODEL_NAME}."
  exit 1
fi

echo "[FINISH] Installation is complete."