#!/bin/bash

source venv/bin/activate
PWD=$(pwd)/../
. common.sh

cd ../
python3 cli.py
