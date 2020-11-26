#! /bin/bash

cd frontend/
pip3 install -r requirements.txt
python3 -m pytest --cov . 

cd ..

cd backend/
pip3 install -r requirements.txt
python3 -m pytest --cov .

