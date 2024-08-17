#!/bin/bash

conda activate .././env &
uvicorn db:app --reload &
python3 .././main.py
