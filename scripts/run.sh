#!/usr/bin/env bash

set -e

JOB="entrypoints/post_stats.py"
INPUT_FILE_PATH="./resources/input_stats_20220907"
CHECKPOINT_DIR="./checkpoints"

echo "JOB: ${JOB}"
echo "INPUT_FILE_PATH: ${INPUT_FILE_PATH}"
echo "CHECKPOINT_DIR: ${CHECKPOINT_DIR}"

export PYTHONPATH=$(pwd)

[[ -d "${CHECKPOINT_DIR}" ]] || mkdir -p "${CHECKPOINT_DIR}"

python $JOB \
    ${INPUT_FILE_PATH} \
    ${CHECKPOINT_DIR}
