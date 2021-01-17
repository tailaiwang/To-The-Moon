#!/usr/bin/env bash

readonly sourceFile="./venv/bin/activate"

source ${sourceFile}

flask run > log.txt 2> error.txt