#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

TRAIN_DATA_ROOT=./bakedata/train/
VAL_DATA_ROOT=./bakedata/val/
TEST_DATA_ROOT=./bakedata/test/

echo "Creating training lmdb..."
GLOG_logtostderr=1 convert_imageset \
    --shuffle \
    --backend="leveldb" \
    $TRAIN_DATA_ROOT \
    $1 \
    ./train_leveldb

echo "Creating validation lmdb..."
GLOG_logtostderr=1 convert_imageset \
    --shuffle \
    --backend="leveldb" \
    $VAL_DATA_ROOT \
    $2 \
    ./val_leveldb

echo "Creating testing lmdb..."
GLOG_logtostderr=1 convert_imageset \
    --shuffle \
    --backend="leveldb" \
    $TEST_DATA_ROOT \
    $3 \
    ./test_leveldb

echo "Done."
