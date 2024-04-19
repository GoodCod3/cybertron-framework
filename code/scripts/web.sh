#!/bin/bash

cd ../
source venv/bin/activate
export FLASK_APP=web
export FLASK_ENV=development
PWD=$(pwd)
. ./scripts/common.sh

flask run --debugger
