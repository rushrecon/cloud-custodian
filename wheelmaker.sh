#!/bin/bash

export ROOT_DIR=$1

export TARGET_DIR=$ROOT_DIR/cloud-custodian/bazel-bin/
export SETUP_PATH=$ROOT_DIR/cloud-custodian/$2/setup.py
export SOURCE_ENV=$ROOT_DIR/venv/bin/activate

cd $ROOT_DIR

echo `pwd`

source $1

python3 $SETUP_PATH sdist bdist_wheel -d $TARGET_DIR # > /dev/null > 2&>1

#rm -r $TARGET_DIR/*

find $TARGET_DIR ! -name *.whl -type f -exec rm -f {} +
