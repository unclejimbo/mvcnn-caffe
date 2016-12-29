#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

TRAIN_DATA_ROOT=./bakedata/train/
VAL_DATA_ROOT=./bakedata/val/
TEST_DATA_ROOT=./bakedata/test/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=256
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

echo "Creating training lmdb..."
GLOG_logtostderr=1 convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --backend="leveldb" \
    $TRAIN_DATA_ROOT \
    ./train_one_third.txt \
    ./train_one_third_leveldb

echo "Creating validation lmdb..."
GLOG_logtostderr=1 convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --backend="leveldb" \
    $VAL_DATA_ROOT \
    ./val_one_third.txt \
    ./val_one_third_leveldb

echo "Creating testing lmdb..."
GLOG_logtostderr=1 convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --backend="leveldb" \
    $TEST_DATA_ROOT \
    ./test_one_third.txt \
    ./test_ont_third_leveldb

echo "Done."
